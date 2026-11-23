
"""









/speckit.specify

# Feature 01: User Authentication
## Project: TruckMitr Loading Module

### Objective
Develop a secure, reliable, and production-ready authentication system for the TruckMitr Loading Module website.

The authentication system must allow authorized users to securely access the application and protect all restricted pages and backend APIs.

### 1. Secure Login
- Provide a professional and responsive login interface.
- Allow authorized users to log in using their approved credentials.
- Validate required login fields.
- Validate user credentials securely.
- Display appropriate validation and authentication error messages.
- Prevent unauthorized users from accessing the application.
- Prevent sensitive information from being exposed through error messages.
- Provide appropriate loading and submission states.

### 2. Secure Logout
- Allow authenticated users to log out securely.
- Invalidate the active session or authentication token.
- Clear authentication-related client-side state securely.
- Prevent access to protected pages after logout.
- Redirect users to the login page after successful logout.
- Handle logout requests and failures appropriately.

### 3. Session / Token Management
- Maintain authenticated user sessions securely.
- Handle session expiration.
- Handle invalid, expired, and revoked tokens.
- Implement secure session/token lifecycle management.
- Prevent unauthorized session reuse.
- Handle authentication across page refreshes.
- Define appropriate session timeout behavior.
- Protect sensitive authentication information.
- Consider concurrent login and multiple-device scenarios.

### 4. Authentication Validation
- Validate user credentials on the backend.
- Validate incoming authentication requests.
- Reject invalid credentials.
- Handle inactive, blocked, or deactivated accounts.
- Prevent unauthorized authentication attempts.
- Apply appropriate login attempt restrictions and rate limiting.
- Provide meaningful and secure error responses.
- Never expose passwords, tokens, or sensitive authentication details.

### 5. Protected Routes and APIs
- Prevent unauthenticated users from accessing protected frontend pages.
- Protect backend APIs against unauthorized requests.
- Redirect unauthenticated users to the login page.
- Validate authentication on every protected backend request.
- Handle expired or invalid sessions consistently.
- Ensure frontend route protection is not treated as a replacement for backend authorization.

### 6. User Experience
- Create a clean, modern, professional login page.
- Maintain consistent TruckMitr branding.
- Provide responsive layouts for desktop, tablet, and mobile.
- Include appropriate form validation.
- Display loading, success, and error states.
- Prevent accidental duplicate form submissions.
- Provide clear feedback for authentication failures.

### 7. Security Requirements
- Follow OWASP authentication security recommendations.
- Never store plaintext passwords.
- Use secure password verification.
- Protect authentication tokens and sessions.
- Prevent brute-force attacks.
- Prevent session fixation.
- Protect against common web authentication vulnerabilities.
- Use secure cookie settings when cookie-based authentication is selected.
- Never expose secrets or credentials in frontend code, logs, or API responses.

### 8. Existing Project Compatibility
Before defining requirements and proposing changes:

- Inspect the existing project structure.
- Identify the actual frontend and backend technologies.
- Investigate existing authentication implementations.
- Inspect existing user tables and database relationships, if accessible.
- Identify existing login APIs and authentication services.
- Understand existing TruckMitr user management.
- Identify whether existing authentication can be reused.

Do not assume the technology stack, database schema, API endpoints, user roles, or authentication mechanism.

Avoid duplicating existing TruckMitr authentication functionality.

### 9. Acceptance Criteria

The feature will be considered functionally complete when:

- Authorized users can log in successfully.
- Invalid credentials are rejected.
- Inactive or unauthorized users cannot log in.
- Authenticated users can access protected pages.
- Unauthenticated users cannot access protected pages or APIs.
- Users can log out successfully.
- Logged-out sessions or tokens cannot be reused.
- Expired sessions are handled correctly.
- Authentication persists correctly according to the selected session strategy.
- Backend authentication validation works correctly.
- Appropriate security and validation tests pass.
- The login interface works across supported screen sizes.

### 10. Specification Guidelines

- Focus on WHAT the authentication system must do, not HOW it will be technically implemented.
- Define clear user stories and acceptance scenarios.
- Identify functional and non-functional requirements.
- Include important edge cases and failure scenarios.
- Avoid vague or conflicting requirements.
- Follow the project constitution.
- Maintain compatibility with existing TruckMitr business workflows.

IMPORTANT:
Do not modify source code during this specification phase.

Do not start implementation.

Generate a complete, clear, and testable feature specification that can be used in the subsequent Clarify, Plan, Tasks, Analyze, and Implement stages.







============================= For Claude ==================================


/speckit.specify

I want to implement Feature 01: User Authentication for the TruckMitr Loading Module.

Develop a secure, reliable, scalable, and production-ready authentication system.

### 1. Secure Login
- Create a professional and responsive login interface.
- Allow authorized users to log in using approved credentials.
- Validate required login fields.
- Verify credentials securely on the backend.
- Display appropriate validation and authentication errors.
- Prevent unauthorized users from accessing the application.
- Provide loading and submission states.

### 2. Secure Logout
- Allow authenticated users to log out securely.
- Invalidate active sessions or authentication tokens.
- Clear authentication-related client-side state.
- Prevent access to protected pages after logout.
- Redirect users to the login page.
- Handle logout failures appropriately.

### 3. Session / Token Management
- Maintain authenticated sessions securely.
- Handle session expiration.
- Handle invalid, expired, and revoked tokens.
- Manage authentication lifecycle securely.
- Handle page refresh without unexpectedly losing valid authentication.
- Define appropriate session timeout behavior.
- Consider concurrent sessions and multiple-device login.

### 4. Authentication Validation
- Validate credentials on the backend.
- Reject invalid credentials.
- Handle inactive, blocked, and deactivated accounts.
- Prevent unauthorized authentication attempts.
- Apply appropriate rate limiting and brute-force protection.
- Return consistent and secure error responses.
- Never expose passwords, tokens, or sensitive authentication information.

### 5. Protected Routes and APIs
- Protect all authenticated frontend routes.
- Protect backend APIs against unauthorized requests.
- Redirect unauthenticated users to the login page.
- Validate authentication on protected API requests.
- Handle expired and invalid sessions consistently.
- Never rely exclusively on frontend route protection for security.

### 6. User Experience
- Follow professional enterprise-grade UI/UX standards.
- Maintain consistent TruckMitr branding.
- Support desktop, tablet, and mobile devices.
- Implement proper form validation.
- Provide loading, success, and error states.
- Prevent duplicate form submissions.

### 7. Security Requirements
- Follow OWASP authentication security recommendations.
- Never store plaintext passwords.
- Use secure password verification.
- Protect sessions and authentication tokens.
- Prevent brute-force attacks and session fixation.
- Use secure cookie settings when applicable.
- Never expose credentials or secrets in frontend code, logs, or API responses.

### 8. Existing Project Investigation

Before defining the specification:

- Inspect the complete existing project structure.
- Identify actual frontend and backend technologies.
- Investigate existing authentication implementations.
- Inspect existing user tables and database relationships, if accessible.
- Identify existing authentication APIs and services.
- Understand existing TruckMitr user management.
- Determine whether existing authentication can be reused.

Do not assume the technology stack, database schema, API endpoints, user roles, or authentication mechanism.

Avoid duplicating existing TruckMitr functionality.

### 9. Acceptance Criteria

The feature must satisfy the following:

- Authorized users can log in successfully.
- Invalid credentials are rejected.
- Inactive or unauthorized users cannot log in.
- Authenticated users can access protected pages.
- Unauthenticated users cannot access protected pages or APIs.
- Users can log out successfully.
- Invalidated sessions or tokens cannot be reused.
- Expired sessions are handled correctly.
- Authentication works correctly after page refresh.
- Backend authentication validation works correctly.
- Security and validation tests pass.
- Login interface works across supported screen sizes.

### 10. Specification Instructions

Act as a senior product manager, software architect, frontend engineer, backend engineer, database architect, and security engineer.

- Follow the project constitution.
- Define clear user stories.
- Define measurable functional requirements.
- Define non-functional requirements.
- Include acceptance scenarios.
- Identify edge cases and failure scenarios.
- Identify dependencies and business constraints.
- Ensure requirements are testable and unambiguous.

Focus on WHAT the system must do, not HOW it will be implemented.

Do not modify source code.
Do not implement the feature during this stage.

Generate a complete, production-oriented User Authentication specification that will be used in the subsequent Clarify, Plan, Tasks, Analyze, and Implement stages.






















"""
