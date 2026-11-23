
"""










# Updated Spec Kit Workflow – Existing Feature

## Feature 01: User Authentication

Objective:
Update the existing authentication feature to support mobile number + third-party OTP authentication.

Restart from the earliest stage affected by the requirements change.

---

### 1. Constitution

Purpose:
Establish project-wide engineering principles and development standards.

Main Command:
/speckit.constitution

After completing the Constitution:
- Review the generated constitution.md.
- Verify the technology stack, security standards, architecture principles, coding standards, and database guidelines.
- Correct any missing or incorrect principles before proceeding.

Next Command:
/speckit.specify

Note:
Run the Constitution command once per project. Update it only when project-wide principles or standards change.

---

### 2. Specify

Purpose:
Define the functional and non-functional requirements for mobile number + third-party OTP authentication.

Main Command:
/speckit.specify

After completing Specify:
- Review spec.md.
- Verify user stories and acceptance criteria.
- Check login, OTP verification, resend OTP, logout, and session requirements.
- Verify security and error-handling requirements.
- Remove outdated password-based requirements where they conflict.
- Identify unclear or missing requirements.

Next Command:
/speckit.clarify

---

### 3. Clarify

Purpose:
Resolve ambiguities and finalize authentication requirements.

Main Command:
/speckit.clarify

After completing Clarify:
- Review all clarification questions and answers.
- Verify OTP provider requirements.
- Confirm OTP expiry, resend cooldown, and attempt limits.
- Confirm mobile number and country-code rules.
- Confirm account eligibility and user status handling.
- Confirm session expiry and multiple-device policy.
- Verify that approved clarifications are reflected in spec.md.

Next Command:
/speckit.plan

---

### 4. Plan

Purpose:
Define the technical architecture and implementation approach.

Main Command:
/speckit.plan

After completing Plan:
- Review plan.md.
- Verify frontend and backend architecture.
- Review API design and authentication flow.
- Review database changes and migrations.
- Verify third-party OTP provider integration.
- Review security, session management, and error handling.
- Confirm alignment with the approved technology stack.
- Identify unresolved technical decisions.

Next Command:
/speckit.checklist

---

### 5. Checklist

Purpose:
Validate the completeness and quality of the requirements.

Main Command:
/speckit.checklist

After completing Checklist:
- Review the generated requirements checklist.
- Verify requirement clarity and testability.
- Check security and OTP edge cases.
- Check acceptance criteria and missing scenarios.
- Resolve identified requirement gaps.
- Update the specification if necessary.

Next Command:
/speckit.tasks

Note:
The checklist validates requirement quality. It does not confirm that implementation or testing is complete.

---

### 6. Tasks

Purpose:
Generate an implementation task list from the approved specification and technical plan.

Main Command:
/speckit.tasks

After completing Tasks:
- Review tasks.md.
- Verify frontend, backend, database, and OTP integration tasks.
- Check security and automated testing tasks.
- Verify task dependencies and execution order.
- Remove outdated tasks.
- Confirm every important requirement has corresponding implementation tasks.

Next Command:
/speckit.analyze

---

### 7. Analyze

Purpose:
Check consistency across specification, plan, and implementation tasks.

Main Command:
/speckit.analyze

After completing Analyze:
- Review all analysis findings.
- Resolve specification, planning, and task inconsistencies.
- Identify missing requirements or implementation tasks.
- Check for technical conflicts and security gaps.
- Update the relevant artifacts.
- Run Analyze again until critical findings are resolved.

Next Command:
/speckit.implement

---

### 8. Implement

Purpose:
Implement the approved authentication feature.

Main Command:
/speckit.implement

After completing Implementation:
- Review the implemented frontend and backend code.
- Verify database migrations and relationships.
- Test OTP request, verification, expiry, and resend.
- Test login, logout, and protected routes/APIs.
- Verify session management and security controls.
- Run automated tests.
- Fix failed tests and incomplete functionality.

Next Command:
/speckit.converge

---

### 9. Converge

Purpose:
Verify the actual implementation against the specification, plan, and tasks.

Main Command:
/speckit.converge

After completing Converge:
- Review implementation gaps.
- Check incomplete or missing functionality.
- Verify specification and plan compliance.
- Review any newly appended tasks.
- Execute remaining tasks using:
/speckit.implement
- Run Converge again until all requirements are satisfied.

---

## Final Workflow

1. /speckit.constitution
2. /speckit.specify
3. /speckit.clarify
4. /speckit.plan
5. /speckit.checklist
6. /speckit.tasks
7. /speckit.analyze
8. /speckit.implement
9. /speckit.converge

## Important Rules

- Update the existing Feature 01; do not create a duplicate feature.
- Preserve previously approved requirements that remain relevant.
- Update dependent artifacts whenever requirements change.
- Review each generated artifact before proceeding.
- Do not start implementation until tasks and analysis findings are reviewed.
- Repeat implementation and convergence until the feature is complete.













"""










