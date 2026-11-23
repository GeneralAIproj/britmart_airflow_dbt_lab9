# Learning Notes — BritMart Airflow & dbt Lab

Use this file to collect concepts, questions, comparisons, and things to revisit while working through the lab.

The goal is to keep the practical work moving without losing interesting questions along the way.

---

## 1. Questions to revisit

### dbt materializations vs. Dataform

**Question:** How does dbt's concept of *materialization* compare with the equivalent functionality in Google Cloud Dataform?

Things to investigate:

- What does dbt mean by materialization?
- What are the available dbt materializations?
  - View
  - Table
  - Incremental
  - Ephemeral
- How does Dataform handle tables, views, and incremental tables?
- Are the concepts functionally equivalent, or are there important differences?
- How do dbt and Dataform decide when to rebuild or update a model?
- How does this affect performance, storage, and execution costs?

**Initial observation:**

In the current `dbt_project.yml`, the example models are configured with:

```yaml
models:
  britmart_pipeline_dbt:
    example:
      +materialized: view
```

This means dbt creates views by default for models in the `example` directory, unless a model overrides that configuration.

**My comparison with Dataform:**

_To be completed._

---

## 2. Concepts explained

Use this section for explanations that are worth keeping as reference material.

### Concept: 

**Explanation:**

**Example:**

**Why it matters:**

---

## 3. Comparisons with other technologies

Use this section to connect new concepts to tools and technologies I've used before.

### Technology comparison

**Concept:**

**Tool A:**

**Tool B:**

**Similarities:**

**Differences:**

**Practical implications:**

---

## 4. Questions that come up during the lab

These don't necessarily need to be answered immediately. Add them here and return to them when there's time.

- [ ] 

---

## 5. Things to investigate later

Topics that are interesting but aren't necessary to complete the current exercise.

- [ ] 

---

## 6. Practical lessons and mistakes

Record errors, fixes, and useful commands so I can understand what happened if I encounter the same problem again.

### Issue:

**What happened:**

**Cause:**

**Solution:**

**What I learned:**

---

## 7. General observations

Anything else worth remembering about the architecture, workflow, or tools.

- 
