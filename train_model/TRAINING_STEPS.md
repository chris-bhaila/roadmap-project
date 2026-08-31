# How the Career-Path Model Was Trained

This document explains, in plain language, everything that was done to turn raw survey
data into the model that predicts a student's top 5 likely career paths. It follows the
same order as the steps in `train.ipynb`.

## 1. Start with the raw data

The starting point was a large developer survey export with **172 columns** and many
rows — one row per person who took the survey. Most of those columns are about a
person's *current job* (salary, employer, remote work setup, opinions about tools).
A student doesn't have any of that information about themselves yet, so it can't be
used to predict their future career.

Only **8 columns** describe things a student actually *can* answer about themselves:
- Education level
- Years of coding experience
- Programming languages they've used
- Databases they've used
- Platforms/cloud tools they've used
- Web frameworks they've used
- Their current main activity (student, professional, etc.)
- Their job role (this is what the model will try to predict)

Every other column was thrown away.

## 2. Keep only rows that are actually useful for learning

- **Only working professionals were kept.** Someone has to already be working in a
  role for their skills to tell us anything real about "these skills → this job."
  Students, hobbyists, and retirees were removed.
- **Some job roles were removed as targets**, because they don't make sense as
  something to recommend to a student: "Student" (circular), "Retired," "Senior
  executive," "Founder," and "Other" (too vague/undefined).
- **Rows with an unclear education answer** ("Other, please specify") were removed,
  since there's no way to rank that answer against the other education levels.
- **Rows missing any needed answer** were removed entirely, rather than guessing
  a value for the blank. This keeps the data honest — nothing was invented.
- **Job roles with too few examples** (fewer than 50 people in that role) were
  dropped, because there isn't enough data to reliably learn a pattern for them,
  or to fairly check if the model got them right later.

## 3. Clean up unrealistic answers

Some people answered "100 years" of coding experience, which isn't realistic for
anyone, including older respondents. To fix this without a complicated check, any
answer above **40 years** was simply capped at 40.

## 4. Turn the answers into numbers the model can use

Models can't work with text answers directly, so everything was converted to numbers:

- **Education level** was converted to a single number from 1 (elementary school) to
  7 (professional degree like a PhD or MD), because education has a natural order —
  a bachelor's degree is "more" than a high school diploma. Keeping it as one ordered
  number lets the model ask simple questions like "did they get at least a bachelor's?"
- **Skills** (languages, databases, platforms, frameworks) work differently — someone
  can know many of them at once, and there's no natural ranking between "Python" and
  "Java." So each individual skill became its own **yes/no column** (1 if they know
  it, 0 if they don't). For example, "knows Python" became its own column separate
  from "knows JavaScript."

No further number-scaling was needed, because the type of model used (decision
tree, explained below) only ever asks yes/no or threshold questions like "is this
number above X?" — it doesn't care whether numbers are big or small the way some
other model types do.

The one column used earlier just to filter out non-professionals was then removed,
since after filtering, every remaining row had the same value in it and it had
nothing left to teach the model.

The cleaned, fully-numeric data was saved as `training_data_final.csv`.

## 5. Split the data into a training set and a test set

Before building anything, the data was split into two parts:
- **80%** to train the model (let it learn patterns)
- **20%** to test the model afterward (check how well it actually learned, using
  data it has never seen)

This split was done carefully so that every job role kept roughly the same
percentage in both the training set and the test set — otherwise a small role
could end up almost entirely in one side by chance, making it impossible to
train or test fairly on that role.

## 6. Balance out the fact that some job roles are far more common than others

Some roles (like "Full-Stack Developer") had thousands of examples, while others
had only a few dozen. Left alone, a model would just learn to always guess the
most common role and largely ignore the rare ones, since that "cheats" its way
to a low error rate.

To fix this, each role was given a **weight** based on how rare it is — mistakes
on rare roles count for more than mistakes on common roles. This makes the model
actually try to learn the patterns for smaller roles too, not just the biggest one.

(Later in the process, this weighting was fine-tuned — see Step 9.)

## 7. Build the model: a decision tree

The model used here is a **decision tree**, built entirely from scratch (not
using a ready-made library, so the process could be fully understood and
verified step by step).

In plain terms, a decision tree works like a game of 20 questions:
- It looks at all the answers (skills, education, experience) and finds the single
  yes/no or threshold question that best splits people into more "alike" groups —
  for example, "do they know Swift?" or "do they have more than 5 years of
  experience?"
- It repeats this process on each smaller group, asking a new best question each
  time, splitting groups into smaller and smaller, more consistent groups.
- It stops splitting a group once: the group only contains one type of job role
  already, the group has gotten very small, or it has asked 12 questions deep
  in a row (this depth limit stops the model from getting *too* specific and
  just memorizing individual people instead of learning general patterns).
- Each final group ("leaf") remembers what mix of job roles ended up there. That
  mix of roles is what turns into a ranked list of predictions for anyone who
  ends up in that group.

The "best question" at each step is chosen using a measure called **Gini
impurity** — basically a score for "how mixed up is this group of job roles
right now?" A group with only one job role in it scores 0 (perfectly sorted).
A group with lots of different roles evenly mixed scores close to 1. The tree
always picks whichever question shrinks that mixed-up-ness the most.

## 8. Make sure the model always gives 5 suggestions, not fewer

The whole point of this model is to hand a student a **top 5 list** of likely
career paths, not just one guess. But some of the tree's smaller groups
("leaves") ended up with fewer than 5 different roles in them, since a very
specific group of people might really only contain 2 or 3 roles.

To fix this, the model was changed to also remember the role mix at every step
along the way, not just at the very end. If a leaf doesn't have 5 roles in it,
the model "borrows" a bit of the missing roles from a broader group one step
back up the tree (scaled down, so its own genuine matches still rank highest).
This guarantees a real top-5 list can always be produced.

## 9. Check the model's own code for bugs

Since the tree was built from scratch instead of using an existing tool, it
was double-checked against a well-known, trusted library version of the same
kind of model (`scikit-learn`'s `DecisionTreeClassifier`), using the exact
same data and settings. The two produced similar results, which is good
evidence the from-scratch version was built correctly and not silently broken.

## 10. Measure how good the model actually is

Several different scores were used, because no single score tells the whole
story:

- **Top-1 accuracy** — how often the model's single best guess was exactly
  right. This is the strict, traditional way to score a model.
- **Top-5 accuracy** — how often the correct answer showed up *anywhere* in
  the 5 suggestions. This is the number that matters most here, since the
  student sees 5 options, not 1.
- **Precision, recall, and F1 score, averaged equally across every job role**
  (called "macro-averaging") — this stops the score from being dominated by
  the most common role and hides how badly the model is doing on rarer roles.
- **A results table for each individual job role** — showing exactly which
  roles the model is good or bad at, sorted worst-to-best, so problem areas
  are obvious rather than hidden inside one overall number.
- **A confusion matrix** — a chart showing which roles get mixed up with which
  other roles (e.g., is "Back-End Developer" often mistaken for "Full-Stack
  Developer"?). Mix-ups between closely related roles are expected and not
  a real problem; mix-ups between unrelated roles would be a red flag.
- **A comparison against a "dumb" baseline** — what if the model just always
  guessed the most common role(s) for everyone, ignoring their actual skills?
  If the real model can't beat that lazy approach, it isn't actually learning
  anything useful about the individual student.

## 11. Fix a problem the metrics revealed

The first version of the model actually **tied with the lazy "always guess
the most common roles" baseline** on the top-5 score. Digging into why showed
that the earlier rare-role weighting (Step 6) had gone too far — it made
mistakes on the biggest role ("Full-Stack Developer") count for almost
nothing, so the model started avoiding predicting it even when it was
clearly correct.

The fix was to soften the weighting formula (using a square root instead of
the raw ratio), so rare roles still get extra attention, but not so much
that the model swings too far the other way. This was tested against a
couple of other in-between weighting strengths too, and the softened version
performed best.

## 12. Tune the model's settings (avoid over- or under-learning)

A few more settings were experimented with to find the best balance:

- **Tree depth** — going deeper (allowing more questions in a row) was tried,
  but it caused the model to start memorizing quirks of the training data
  instead of learning general patterns (this is called **overfitting** — the
  model looks great on data it has already seen, but does worse on new data).
  The shallower setting performed better on new, unseen data.
- **Minimum group size before splitting** — instead of going deeper, the model
  was told to require a bigger group of people before it's allowed to ask
  another question. Requiring larger groups (50 people minimum, instead of
  10) reduced overfitting and gave the best overall test results.

## 13. Lock in the final settings

After all that testing, the final, official configuration was:
- Maximum of 12 questions deep
- Require at least 50 people in a group before splitting it further
- Softened (square-root) weighting for rare job roles

On data the model had never seen before, this version reached:
- **Top-5 accuracy: 84.38%** — the correct career role appeared in the
  student's top 5 suggestions about 84 times out of 100.
- **Top-1 accuracy: 38.16%** — the single best guess was exactly right about
  38 times out of 100.
- **Macro F1 score: 0.1627** — reflects that performance is still notably
  uneven across the 18 possible roles, with some roles predicted far more
  reliably than others (a fair, known limitation given how little data some
  rarer roles have).

These are the honest, official numbers, produced only from data the model
never got to train on.

## 14. Prepare the final model for real use

Once the settings were locked in and the honest scores were recorded, the
model was **retrained one more time using all of the data** (the training
data and the testing data combined), so the version that actually gets used
by students has learned from as many real examples as possible. This is a
standard, accepted last step — the earlier train/test split had already done
its job of producing trustworthy scores, so nothing further needed to be
proven at this point.

Finally, the finished model was saved to a file, along with:
- The settings it was trained with
- Its official test scores (listed above)
- The exact list of every skill/answer column it expects, so the website's
  sign-up form can be built to collect exactly the right information from
  each student.
