"""











/speckit.plan

# Update Existing Feature 01: User Authentication – Technical Implementation Plan

I want to update the existing technical implementation plan for Feature 01: User Authentication in the TruckMitr Loading Module.

## Important Project Context

This is an update to an existing feature, not a new feature.

The authentication approach has changed to:

**Mobile Number + Third-Party OTP Authentication**

The system must authenticate eligible users using their mobile numbers and OTP verification through a third-party OTP service provider.

Preserve the existing feature identity, approved requirements, and clarification decisions.

Do not create duplicate plan files.

## 1. Fixed Technology Stack

Use the following approved technology stack:

Frontend:
- Next.js
- TypeScript
- Next.js App Router
- Tailwind CSS


Backend:
- Laravel
- PHP
- RESTful APIs

Database:
- MySQL
- Laravel Migrations

Authentication:
- Laravel Sanctum, subject to the confirmed deployment architecture.
- Secure cookie-based authentication where applicable.


Development Tools:
- Git and GitHub
- npm
- Postman
- phpMyAdmin


Do not replace the approved technology stack without identifying a genuine technical blocker.

## 2. Authentication Architecture

Design the complete mobile OTP authentication architecture.

Include:

- Mobile number submission.
- Mobile number validation.
- Existing user/account verification.
- OTP generation request.
- Third-party OTP provider integration.
- OTP delivery handling.
- OTP verification.
- Authentication session creation.
- Current authenticated user retrieval.
- Secure logout.
- Protected frontend routes.
- Protected backend APIs.

Define the complete request and response flow between Next.js, Laravel, MySQL, and the third-party OTP provider.

## 3. Third-Party OTP Integration Architecture

Design a provider-independent OTP integration.

Include:

- OTP provider adapter/service.
- Provider API communication.
- Secure provider credential management.
- OTP generation request.
- OTP verification request.
- Provider response handling.
- Delivery status handling, where supported.
- API timeout handling.
- Provider failure handling.
- Retry strategy where safe.
- Provider response normalization.

Keep provider-specific logic separate from authentication business logic.

Do not invent provider API endpoints or request formats.

Use the confirmed provider documentation when available.

If the provider is not finalized, define an abstraction and clearly document the remaining integration dependency.

## 4. Backend API Design

Define the required REST API endpoints.

Consider:

- Request OTP.
- Verify OTP.
- Resend OTP, if separate from request OTP.
- Retrieve authenticated user.
- Logout.
- Session validation, if required.

For each endpoint document:

- HTTP method.
- URL.
- Request parameters.
- Validation rules.
- Authentication requirements.
- Response structure.
- HTTP status codes.
- Error responses.
- Rate-limiting rules.

Ensure API design follows the existing project conventions.

## 5. Database Architecture

Review the clarified requirements and define the necessary MySQL database changes.

Consider:

- Existing users table structure.
- Mobile number storage.
- Country code storage or normalization.
- Mobile number uniqueness.
- Account status.
- OTP challenge or request tracking, if required.
- OTP verification attempt tracking, if required.
- Authentication session management.
- Audit information.

Define:

- Tables and columns.
- Data types.
- Primary and foreign keys.
- Relationships.
- Indexes.
- Constraints.
- Laravel migrations.

Do not store plaintext OTPs or unnecessary sensitive information.

Avoid duplicating user information or creating unnecessary tables.

Explain which OTP responsibilities belong to the third-party provider and which belong to the application.

## 6. Frontend Implementation Architecture

Design the Next.js authentication experience.

Include:

- Mobile number login page.
- Country code selector.
- Mobile number validation.
- Request OTP action.
- OTP verification page.
- OTP input component.
- Resend OTP countdown.
- Loading states.
- Error and success messages.
- Authentication state management.
- Secure session persistence.
- Protected route handling.
- Logout functionality.
- Session expiration handling.

Use reusable components and maintain consistent TruckMitr branding.

## 7. Backend Implementation Architecture

Define the Laravel backend components.

Consider:

- Authentication controller.
- Authentication service.
- OTP service.
- Third-party provider adapter.
- Provider configuration.
- Request validation.
- Authentication middleware.
- Rate-limiting middleware.
- Session management.
- Standardized API responses.
- Centralized exception handling.

Keep controllers thin and business logic in appropriate service classes.

Follow Laravel coding standards and maintainable architecture.

## 8. Security Architecture

Design security controls for OTP authentication.

Include:

- OTP expiration.
- Verification attempt restrictions.
- OTP resend cooldown.
- OTP request rate limiting.
- Brute-force protection.
- OTP replay prevention.
- Secure provider credential storage.
- API timeout and failure handling.
- Account enumeration protection.
- Secure session management.
- Secure cookies and CSRF protection where applicable.
- Sensitive information masking.
- Authentication audit logging.

Never expose OTP values, provider credentials, authentication tokens, or secrets in logs or API responses.

## 9. Testing Strategy

Define a complete testing strategy.

Include:

Unit Tests:
- Mobile number validation.
- OTP service.
- Provider adapter.
- Authentication service.

Integration Tests:
- OTP request API.
- OTP verification API.
- Provider API integration.
- Session creation.
- Logout.
- Protected APIs.

Frontend Tests:
- Mobile number form.
- OTP input.
- Resend countdown.
- Loading and error states.
- Authentication redirects.

Security Tests:
- Invalid OTP.
- Expired OTP.
- Repeated verification attempts.
- Excessive OTP requests.
- Unauthorized access.
- Provider failures.
- Session expiration.
- OTP replay attempts.

Use mocked provider responses for automated tests so external OTP API availability is not required for every test.

## 10. Implementation Sequence

Create an implementation sequence with dependencies:

1. Authentication architecture and configuration.
2. Database design and migrations.
3. OTP provider integration interface.
4. Third-party OTP provider implementation.
5. Mobile number validation.
6. OTP request API.
7. OTP verification API.
8. Authentication session management.
9. Logout API.
10. Frontend mobile login interface.
11. Frontend OTP verification interface.
12. Protected frontend routes.
13. Protected backend APIs.
14. Security controls.
15. Automated testing and verification.

Adjust the sequence according to actual dependencies.

## 11. Important Instructions

- Follow the existing project constitution.
- Follow the updated User Authentication specification.
- Follow all confirmed clarification decisions.
- Preserve the approved technology stack.
- Update the existing technical plan rather than creating a new feature.
- Do not create duplicate plan files.
- Do not assume OTP provider capabilities.
- Do not invent third-party API documentation.
- Do not introduce unnecessary technologies.
- Do not modify application source code.
- Do not implement the feature during planning.

Generate the updated technical implementation plan in the existing Spec Kit plan file.

The plan must be detailed, secure, scalable, and ready for `/speckit.tasks`.














"""