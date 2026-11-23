"""



Spec-Driven Development with claude code
========================================


Step 1 : Product Requirements Document(PRD)
-------------------------------------------

Define What need to be built

. Problem Statement
. Epics (User Stories)
. Business Golals
. Acceptance Criteria
. User Requirements 
. Functional Requirements
. Scope
. Non Functional Requirements
. Risks
. Constraints


Step 2 : Technical Design Document(TDD)
---------------------------------------

Define How it will be built

. Architecture
. Security Design
. Technology Stack
. Development strategy
. API Design


Step 3 : Feature Specification
------------------------------

Define ONE feature in detail

. Feature Description 
. Bounderies
. Requirements
. Acceptance Criteria


For each feature we create two file
.  A Feature file
.  And crossponding plan file





Document Flow
-------------
                                            (What this feature must do)
PRD --------------------> TDD ---------------------> Feature Spec 
(What to build)          (How to build it)               |
                                                         |
                                                         |
Test <------------------ Code <---------------------- Plan
(Verify it works)        (Actual Implementation)      (How claude will implement it)






Step 3 - Detailed Workflow
--------------------------


[Plan the feature] --------> [Create Branch] -------------> [Plan with Claude Code] 
                                                                      |
                                                                      |
[Commit Changes] <-------- [Test the feature] <------------ [Implement the feature]
      |
      |
[Push to Github] ---------> [Create Pull Request] ---------> [Code Review]
                                                                   |
                                                                   |
[Merge PR] <----------- [CICD Pipeline Runs] <------------- [Address Feadback]
     |
     |
Next feature(Pick next feature from PRD/Backlog) 
     |
     |
Repeat Step 3 (For Next Feature)
     |
All Feature Complete
(High Quality Product Delivered)





"""