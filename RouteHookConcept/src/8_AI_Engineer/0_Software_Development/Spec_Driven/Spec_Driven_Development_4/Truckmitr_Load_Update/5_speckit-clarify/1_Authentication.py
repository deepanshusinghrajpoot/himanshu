"""




/speckit.clarify

# Clarify Existing Feature 01: User Authentication

I have updated the existing User Authentication feature of the TruckMitr Loading Module.

The authentication method is now:

Mobile Number + Third-Party OTP Authentication.

Your task is to review the updated authentication specification and identify all ambiguities, missing requirements, conflicting requirements, and unresolved business or technical decisions.

Act as a senior business analyst, software architect, backend engineer, frontend engineer, database architect, and application security engineer.

## 1. Mobile Number Authentication

Clarify:

- Which country codes should be supported?
- Is the application restricted to Indian mobile numbers (+91)?
- Should mobile numbers be unique across user accounts?
- Should only existing registered users be allowed to log in?
- How should unknown mobile numbers be handled?
- How should inactive, blocked, and deactivated accounts be handled?

## 2. Third-Party OTP Provider

Clarify:

- Which third-party OTP service provider will be used?
- Does the provider support OTP generation and verification through APIs?
- Does the provider manage OTP expiration?
- Does the provider support OTP resend?
- Does the provider provide delivery status?
- How should provider downtime and API failures be handled?
- Should the application support changing the OTP provider in the future?

Do not assume a provider or invent its API endpoints.

If the provider is not selected, document this as an unresolved decision and recommend evaluating suitable providers.

## 3. OTP Configuration

Clarify:

- OTP length (4 or 6 digits).
- OTP expiration time.
- OTP resend cooldown.
- Maximum OTP verification attempts.
- Maximum OTP generation requests.
- Maximum resend requests.
- Temporary lockout duration.
- Whether a newly generated OTP invalidates the previous OTP.

Recommend practical defaults where appropriate, but ask for confirmation when business decisions are required.

## 4. OTP Verification

Clarify:

- How OTP verification will be performed.
- How invalid OTPs will be handled.
- How expired OTPs will be handled.
- How repeated incorrect attempts will be restricted.
- How OTP replay attacks will be prevented.
- How verification will behave if the third-party provider is unavailable.
- Whether OTP verification results can be reused.

## 5. User Account Validation

Clarify:

- How the mobile number will be matched to an existing user.
- Whether user registration is outside this feature's scope.
- Whether only active and authorized users can authenticate.
- How blocked and deactivated accounts will be handled.
- Whether additional account verification is required.

## 6. Session and Authentication Management

Clarify:

- Whether Laravel Sanctum cookie-based authentication is suitable for the deployment architecture.
- Session expiration policy.
- Logout behavior.
- Token or session invalidation.
- Multiple-device login policy.
- Concurrent session policy.
- Authentication persistence after page refresh.
- Unauthorized API access behavior.

## 7. Security Requirements

Review:

- OTP rate limiting.
- Brute-force protection.
- Secure provider credential storage.
- API timeout handling.
- Prevention of OTP replay.
- Prevention of account enumeration.
- Secure session management.
- Sensitive information masking.
- Authentication audit logging.

Identify missing security requirements.

## 8. User Experience

Clarify:

- Mobile number entry experience.
- Country code selection.
- OTP entry screen.
- Resend OTP countdown.
- Loading states.
- Invalid OTP messages.
- Expired OTP messages.
- OTP delivery failure messages.
- Session expiration handling.
- Logout and redirection behavior.

## 9. Technical and Business Constraints

- Follow the existing project constitution.
- Follow the fixed technology stack: Next.js, TypeScript, Laravel, PHP, and MySQL.
- Preserve the existing Feature 01 identity.
- Do not create duplicate specification files.
- Do not introduce unrelated features.
- Do not assume unavailable provider capabilities.
- Do not modify source code.
- Do not implement anything during clarification.

## 10. Clarification Instructions

1. Read the updated User Authentication specification.
2. Review the project constitution.
3. Identify all unresolved decisions.
4. Ask focused questions where clarification is necessary.
5. Recommend practical options for each important decision.
6. Update the existing specification with confirmed decisions.
7. Keep unresolved decisions explicitly documented.
8. Ensure requirements and acceptance criteria are testable.

The objective is to produce a complete and unambiguous authentication specification before proceeding to `/speckit.plan`.












"""