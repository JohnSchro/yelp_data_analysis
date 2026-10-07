# DS 6021: Introduction to Predictive Modeling

## Final Project Instructions and Rubric

*Last updated: 8/24/2026*

> Source: [DS_6021_Final Project Rubric.pdf](</Users/johnschroter/Desktop/DS_6021_Final Project Rubric.pdf>). This Markdown transcription includes the full content of all seven pages. Formatting, page breaks, and line-wrap hyphenation have been adapted for readability; the timetable is presented as dated subsections.

## Overview

This project is your opportunity to demonstrate a synthesis of the skills you learn throughout the semester: identifying business problems or research questions that are suitable for solving with predictive modeling, finding reputable data, exploring that data through thoughtful summarization and visualization, building predictive and unsupervised learning models, and presenting results professionally to an audience of your peers.

Please read this rubric carefully. If you have questions at any point throughout the semester, please ask them. Do not put this off until the last minute!

## Learning Objectives

1. **Identify a Problem to Solve.** Define specific research questions or identify a relevant business problem that can be answered in a data-driven way. In many ways, this is the most critical step. What is an unsolved problem that can be meaningfully solved using data and machine learning?

2. **Find a reputable data source.** Your dataset should have at least 4 numeric variables and at least 4 categorical variables. You may also combine multiple datasets that are related to help answer the questions posed in Step 1. This is also very representative of the types of problems you will see in a real-world environment - you rarely need only a single data source! Clearly document your data source(s) and explain why you chose them. You are encouraged to use data engineering techniques such as APIs or web scraping to gather your data.

3. **Apply data engineering and cleaning steps.** Depending on the dataset, this might include renaming columns, removing irrelevant or duplicated rows/columns, mutating variables, creating new features, or subsetting the data to investigate specific questions. All datasets should include at least some element of cleaning and engineering, as this will always happen in a real-world context.

4. **Visualize and summarize** pertinent variables in the data. Your analysis should include a robust set of descriptive statistics and informative visualizations. Do not just generate a lot of plots because you can; choose the ones that are most informative for telling us something about the problem you are solving.

5. **Use predictive models and unsupervised learning** methods covered in the course to investigate your research questions. Use the major models from class as appropriate: e.g., Linear Regression/GLMs, KNN, *k*-means clustering, PCA, and/or tree-based methods. For example, if you choose a binary classification problem, it would not be appropriate to use linear regression, but you should leverage GLMs and classification trees.

6. **Present your work** to the class in an 8-10 slide presentation that should last 12 minutes total. This includes 3-5 minutes at the end for Q&A. The presentation rubric is included below in the Project Deliverables section.

7. **Build an app that showcases your work.** A published app or dashboard should be included to showcase your work. Details are below. This could be a simple interactive dashboard or similar. It does not need to be overengineered to be impactful.

8. **Collaborate with others.** Data science is an inherently collaborative endeavor. You will be working in teams of 3-4 to complete this project.

## Project Deliverables and Due Date

Turn in the following **via Canvas, under Assignments by 11:59 PM on Sunday, 12/6/2026.**

1. Presentation slides saved as a PDF or HTML. If you use Google Slides or PowerPoint, both have options to export as PDF.

2. Original dataset(s) saved as a `.csv` or `.json`. Include both raw and cleaned versions of your data and any code used to transform your data from the raw to cleaned version.

   If you used code to access an API, do web scraping, or similar, please include that as part of the GitHub repository described below. If the dataset is too large for Canvas, please provide a link to an AWS S3 bucket or similar location where it is stored.

   - For purposes of this class, the data you use may be included in your GitHub repository if necessary, but please be advised that this is not a best practice and can sometimes be flagged as a security violation if it includes sensitive data.

3. A link to a GitHub repository with all the code you used in this project. This could include a Python notebook or `.py` files, Markdown, and any compiled code if applicable. All code should be well-commented and reproducible, with instructions on how to run it.

4. A published app (built in Python Dash, Flask, FastAPI, Streamlit, or a similar framework). The app must be deployed publicly so it can be accessed for evaluation.

5. Information about any Generative AI tools you used and how you used them. See below for details.

## Presentation Rubric

1. Your presentation should be somewhere between 8-10 slides.

2. The first slide must include the project title, group number, and list of group members in alphabetical order of last names.

3. The second slide should be an **executive summary** of the project, including the problem you chose, the impact of solving it, and a brief overview of how you solved it, including only key results.

   Executive summaries are just that: summaries for a busy executive who may not have the time or background to ingest all of the details of your project. This slide should be succinct and get at the “so what” without including every detail.

4. Subsequent slides should walk us through the data selected, appropriate summaries and visualizations, predictive and unsupervised learning models you used, etc.

5. The presentation must also include a brief demo of your app.

6. As noted above, presentations should last no longer than 12 minutes, including around 3-5 minutes for Q&A. Practice to ensure you finish on time.

7. Use visuals effectively - avoid cluttered slides and emphasize clarity over quantity. Your slides should generally not be a wall of text.

## A Note About Using Generative AI

If you use Generative AI to complete this project, you must include the following as part of your project deliverables:

1. A document describing how you leveraged AI to help solve these problems.

2. Any AI-generated code needs to be flagged as such in your GitHub repository. If you are using AI-generated code, please include a README or other relevant files (either in GitHub or as part of your summary document) that describe how you tested this code to ensure that the outputs were sound.

3. If you used a specific `CLAUDE.md` or Claude Skills for this project, please include them as part of your GitHub repository, or link to the repository where they are defined.

4. Version your prompts if applicable. Prompt versioning is a rapidly evolving field.

There is a lot of flexibility in this portion of the project. Basically, I am looking to ensure that you used AI thoughtfully and appropriately as a tool, versus outsourcing your own learning or asking it to do the entire project for you.

As one example, building an app might be unfamiliar to you, and the engineering techniques are beyond the scope of this course. GenAI might be a thoughtful building partner to help here.

**Please adhere to the Generative AI usage guidelines outlined in the syllabus.**

## Examples of Machine Learning Apps and Dashboards

The following are examples of interactive machine learning applications. These examples are intended to provide inspiration for how you might communicate your analysis, models, predictions, and insights through an interactive application.

**Your app does not need to replicate the complexity or scope of these examples.** A simple, well-designed application that effectively communicates your analysis and allows a user to interact with your results can be very impactful.

- **[Credit Card Fraud Detection Dashboard](https://musfirah-credit-card-fraud-detection.streamlit.app/)**

  An interactive classification application that compares multiple machine learning models, evaluates predictive performance using metrics such as precision, recall, F1 score, and ROC-AUC, and allows users to generate predictions. This is a good example of communicating the results of a classification problem through an interactive application.

- **[Bank Customer Churn Prediction & Analytics Dashboard](https://bank-customer-churn-prediction0310.streamlit.app/)**

  An end-to-end classification application that combines exploratory data analysis, preprocessing, feature engineering, model building, model evaluation, and interactive churn prediction. This is a good example of how a business problem can be translated into an interactive predictive modeling application.

- **[Car MPG Prediction & Regularization Dashboard](https://car-mpg-regularization-hkvf3drjhcc7tmjj7x3ms6.streamlit.app/)**

  An interactive regression application that compares linear regression, Ridge regression, and Lasso regression for predicting automobile fuel efficiency. The dashboard includes model-performance comparisons, residual analysis, feature importance, and real-time predictions.

- **[OmniPredict AI: End-to-End Machine Learning Dashboard](https://omnipredict-ai-pnkcq9lkykgqpsfpluzhwk.streamlit.app/)**

  A broader machine learning application incorporating regression, classification, ensemble learning, and clustering. It includes interactive model comparison, feature-importance visualization, and predictive analysis, providing an example of how multiple machine learning methods can be integrated within a single application.

*Note: These examples are provided for inspiration only. The goal of your application is not to build a complex software product. Instead, think about how an interactive application can help someone understand your problem, explore your data, interact with your model, or understand the results and implications of your analysis.*

## Evaluation (130 Points Total)

The project and presentation are worth **130 points**. The scores for each group will be based on the following rubric.

### 1. Problem Selection & Explanation (10 pts)

- **0-3:** Problem chosen is poorly chosen and poorly explained. Unclear motivation.
- **4-7:** Problem chosen has some real-world applicability but motivation for choosing is unclear.
- **8-10:** Problem chosen has clear applicability to a real-world scenario and the motivation for selecting this particular problem is very clear.

### 2. Introduction & Dataset Summary (10 pts)

- **0-3:** Minimal introduction; dataset(s) unclear or poorly described. Data not adequate to solve the proposed problem.
- **4-7:** Adequate introduction; dataset(s) described but missing important context.
- **8-10:** Clear and professional introduction; dataset(s) well described (source, variables, rationale). Clear understanding of connections across multiple datasets.

### 3. Visualization & Exploratory Data Analysis (10 pts)

- **0-3:** Trivial questions, poorly designed charts, or an overwhelming number of charts that provide little value.
- **4-7:** Charts answer reasonable questions but lack depth or clarity.
- **8-10:** Insightful questions explored with well-designed, clearly justified charts.

### 4. Data Engineering & Preparation (10 pts)

- **0-3:** Little or no cleaning or preprocessing shown.
- **4-7:** Some cleaning steps applied; limited justification.
- **8-10:** Thorough data preparation (cleaning, transformations, feature engineering) clearly tied to problem statement.

### 5. Predictive Modeling + Unsupervised Learning (50 pts)

- **0-15:** Models improperly selected and evaluated or only a single modeling approach tried. Experiments not tracked. Improper or non-existent evaluation criteria. No attempt or trivial use of dimensionality reduction or clustering techniques.
- **16-35:** More than one modeling approach is attempted and appropriately chosen for the problem space. Experiments are tracked but are difficult to follow. Dimensionality reduction and/or clustering used appropriately but with weak justification or limited interpretation.
- **36-50:** Multiple suitable modeling approaches are tried and the best one is clearly explained. All experiments are clearly tracked and assumptions are well-articulated. Dimensionality reduction and/or clustering are successfully used as part of the modeling approach.

### 6. App/Dashboard & Presentation (20 pts)

- **0-7:** App missing or non-functional, presentation unorganized, incomplete, or not completed in the time allowed.
- **8-14:** App works but with limited functionality; presentation covers main points but with inconsistent or poorly communicated ideas.
- **15-20:** Interactive, polished app; presentation professional, within time, with clear communication.

### 7. Conclusions & Insight (10 pts)

- **0-3:** Findings unjustified, irrelevant, and/or not tied back to the problem statement.
- **4-7:** Findings somewhat tied to questions but depth and insights are limited.
- **8-10:** Findings are coherent, justified, and clearly connected to the problem selection.

### 8. Ambition & Creativity (10 pts)

- **0-3:** Minimum effort; bare-bones scope.
- **4-7:** Reasonable effort; moderate scope.
- **8-10:** Ambitious scope; creative use of methods or data.

**Total Points: 130**

**Note:** The choice of predictive modeling and unsupervised learning techniques will very much depend on the problem you choose. Some techniques you won’t be able to use for your project and that is fine!

As an example, PCA or dimensionality reduction is often used to reduce the feature space for supervised learning tasks. If you try PCA (or another technique) and it does not improve the efficacy of your model, you will not lose any points if you clearly articulate what you tried and why you chose not to use it in your final model.

You will lose points if you don’t try, or if you try and reject the technique without explanation. If you are confused or unsure, please ask!

## Suggested Timetable

By adhering to the schedule below, you should be well-positioned to complete your final project by the stated deadline on 12/6. It is absolutely fine to work ahead, and if you have questions around sequencing please let me know.

Not every aspect of the project is listed below. These dates are intended to help keep you on track so you aren’t scrambling at the last minute.

### Week 3: 9/7-9/11

Select group members for Final Project. Each team should have 3-4 members.

### Week 5: 9/21-9/25

Problem space should be selected, and you should have an idea of the datasets you will use.

### Week 8: 10/12-10/16

Data cleaning and exploration. Note: The task of cleaning and exploring data is never truly “done” and usually continues throughout the model development lifecycle. By the end of Week 8, you should have a very solid understanding of your data and have taken steps for cleaning and imputation (if appropriate).

### Week 10: 10/26-10/30

By the end of Week 10, you should have attempted to build at least one model (either classification or regression) with your data. The midterm is this week, and getting to this stage will help you review and study.

### Week 12: 11/9-11/13

By this point you should have tried at least two modeling techniques (e.g., logistic regression and a classification tree, or linear regression and a regression tree) and started building your app.

Your model doesn’t have to be complete to start scaffolding your app. It is actually great practice to have an end-to-end skeleton in place so you can identify gaps while you are still building the model.

### Week 13: 11/16-11/20

Think about how you will include dimensionality reduction or unsupervised learning in this project and develop a plan for inclusion.

**Final Presentations:** Presentations will be done on the last day of class, **12/7**. We will find a longer chunk of time so we have time for everyone to get through their materials. Details to come.
