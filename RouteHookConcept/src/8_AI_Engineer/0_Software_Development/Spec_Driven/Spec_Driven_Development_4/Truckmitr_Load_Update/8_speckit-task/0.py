"""












/speckit-tasks

Generate or update the implementation task list for the existing Feature 01: User Authentication.

## Objective

Create a complete, dependency-ordered implementation task list for mobile number + third-party OTP authentication.

## Instructions

1. Review the existing project artifacts before generating tasks:
   - constitution.md
   - specs/001-user-auth/spec.md
   - specs/001-user-auth/plan.md
   - specs/001-user-auth/checklists/security.md
   - Any relevant data models, API contracts, and supporting design documents.

2. Treat the updated specification and technical plan as the source of truth.

3. Generate tasks for all approved requirements, including:

   **A. Database and Data Management**
   - Mobile number and country-code storage and normalization.
   - Mobile number uniqueness and account eligibility.
   - OTP challenge state tracking, if required by the approved architecture.
   - Database migrations, indexes, and constraints.
   - Mobile-number privacy classification and secure handling.

   **B. Backend Authentication**
   - Mobile number validation.
   - OTP request and verification APIs.
   - OTP resend and expiration handling.
   - Verification attempt limits and replay prevention.
   - OTP provider adapter/service integration.
   - Provider timeout, failure, and unknown-outcome handling.
   - Secure session/token creation and validation.
   - Logout and session invalidation.
   - Protected API middleware and authorization.

   **C. Security and Abuse Prevention**
   - Account enumeration resistance across response channels.
   - IP-based and mobile-number-based rate limiting.
   - Shared office NAT considerations.
   - OTP guessing and brute-force protection.
   - OTP replay and concurrent verification protection.
   - Credential management and rotation.
   - Secure logging, masking, and data retention.

   **D. Administrator and Account Recovery**
   - First administrator account creation and initial sign-in.
   - Lost-phone and account recovery requirements.
   - Administrative access and account eligibility handling.

   **E. Frontend**
   - Mobile number entry screen.
   - OTP verification screen.
   - OTP resend countdown and states.
   - Loading, error, expired, and retry states.
   - Authenticated route protection.
   - Logout and session-expiry handling.
   - Responsive and accessible UI.

   **F. Testing and Documentation**
   - Backend unit and feature tests.
   - OTP provider mock tests.
   - API integration tests.
   - Frontend component and interaction tests.
   - Authentication and authorization tests.
   - Security and rate-limit tests.
   - End-to-end authentication tests.
   - API documentation updates.

4. Organize tasks into logical phases and user stories.

5. Define dependencies and execution order. Mark parallelizable tasks where appropriate.

6. Every task must:
   - Have a unique task ID.
   - Describe one clear, actionable implementation activity.
   - Identify the relevant component or file area when known.
   - Include test tasks where appropriate.
   - Map back to specification requirements.
   - Be independently verifiable where practical.

7. Follow the approved technology stack:
   - Frontend: Next.js, React, TypeScript, App Router, Tailwind CSS, shadcn/ui.
   - Backend: Laravel, PHP, REST APIs.
   - Database: MySQL, Laravel Migrations, Eloquent ORM.
   - Authentication: Laravel Sanctum only where suitable for the approved deployment architecture.

8. Do not assume an OTP provider has been selected. Keep provider integration provider-independent and create configuration/integration tasks based only on approved requirements. Do not invent provider endpoints or credentials.

9. Do not create duplicate feature directories, specifications, plans, or task files.

10. Do not implement application code while generating tasks.

## Important Review Requirements

- Check the four previously identified documentation gaps:
  1. First administrator onboarding.
  2. Shared office IP rate limiting.
  3. Mobile-number data classification.
  4. FR-012 versus plan conflict concerning unknown OTP delivery outcomes.

- If any issue remains unresolved in the specification or plan, do not invent a decision. Identify the blocker and create a clearly marked decision-dependent task only when appropriate.
- Review the security checklist, but do not mark checklist items as completed.
- Do not treat requirements checklist completion as implementation completion.

## Expected Output

Update the existing tasks.md with:

1. Implementation phases.
2. User-story-based task grouping.
3. Database tasks.
4. Backend API and service tasks.
5. OTP provider integration tasks.
6. Frontend tasks.
7. Security tasks.
8. Testing tasks.
9. Documentation tasks.
10. Dependencies and execution order.
11. Requirement traceability.
12. Unresolved decisions and blockers.

## Final Validation

After generating tasks.md:

- Verify that every approved functional requirement has implementation coverage.
- Verify that every security requirement has corresponding implementation or testing tasks.
- Check for missing dependencies.
- Check for duplicate or outdated tasks.
- Confirm that task IDs are unique and consistently formatted.
- Confirm that the task list is ready for cross-artifact analysis.

Do not run implementation.

Finally, provide a summary of:
- Tasks created or updated.
- Total task count.
- Tasks grouped by phase.
- Unresolved decisions.
- Any requirements without implementation coverage.

Stop after task generation and review.















"""