"""



Spec Kit – Constitution Prompt
==============================


/speckit.constitution

Create a comprehensive, enterprise-grade Project Constitution for the TruckMitr Loading Module Website.

PROJECT CONTEXT:
The project is a web-based Loading Module for TruckMitr, a logistics and transportation platform.

The purpose of this module is to manage loading-related operations, including loading requirements, truck availability, transporter coordination, driver coordination, load assignments, and operational tracking.

The application must be designed as a production-ready, scalable, secure, maintainable, and user-friendly logistics management system.

IMPORTANT ENGINEERING INSTRUCTION:
Before establishing project-specific technical rules, inspect the existing project repository, source code, configuration files, database schema (if accessible), existing APIs, and established coding conventions.

Do not assume the technology stack, existing database structure, business rules, or integrations without verification.

ESTABLISH THE FOLLOWING NON-NEGOTIABLE PRINCIPLES:

1. BUSINESS-FIRST DEVELOPMENT
- Understand TruckMitr's logistics business workflows before implementation.
- Every feature must solve a clearly identified operational problem.
- Maintain consistency across loading, transporter, truck, and driver workflows.
- Avoid implementing features without understanding their business purpose.
- Preserve existing business logic and backward compatibility.

2. SOFTWARE ARCHITECTURE
- Follow clean architecture and separation of concerns.
- Use modular, reusable, loosely coupled components.
- Separate business logic, presentation, data access, and integrations.
- Maintain clear responsibility for every module.
- Avoid unnecessary abstractions and overengineering.

3. FRONTEND ENGINEERING
- Build a modern, responsive, enterprise-grade web application.
- Follow reusable component architecture.
- Maintain consistent layouts, typography, spacing, colors, and interactions.
- Support desktop, tablet, and mobile devices.
- Optimize rendering and application performance.
- Provide loading, empty, error, success, and confirmation states.

4. UI/UX AND PRODUCT DESIGN
- Design an intuitive logistics operations dashboard.
- Prioritize operational efficiency and ease of use.
- Use professional enterprise dashboard design patterns.
- Provide clear data tables, search, filters, sorting, pagination, and relevant summaries.
- Make important operational information easy to identify.
- Avoid unnecessary visual elements and confusing interactions.
- Maintain accessibility and usability standards.

5. LOADING MODULE BUSINESS WORKFLOWS
- Design workflows for loading requirement management.
- Support truck and vehicle availability management where required.
- Support transporter and driver coordination.
- Support load assignment and operational status tracking.
- Maintain accurate loading records and activity history.
- Implement appropriate status transitions and business validations.
- Prevent duplicate or conflicting assignments.
- Maintain traceability of important operational actions.
- Ensure all workflows reflect verified TruckMitr business requirements.

6. DATABASE ENGINEERING
- Inspect the existing database schema before designing or modifying tables.
- Maintain data integrity and referential consistency.
- Use appropriate primary keys, foreign keys, constraints, and indexes.
- Optimize queries for large datasets.
- Avoid N+1 queries and unnecessary database operations.
- Use database transactions for operations requiring atomicity.
- Avoid duplicate or redundant data.
- Never modify existing production data structures without assessing impact.

7. BACKEND ENGINEERING
- Maintain modular and maintainable backend architecture.
- Keep business logic separate from controllers.
- Implement proper validation and exception handling.
- Use database transactions where appropriate.
- Implement efficient data retrieval and processing.
- Maintain structured logging and audit trails.
- Avoid duplicated business logic.

8. API DEVELOPMENT
- Follow consistent REST API conventions where applicable.
- Use appropriate HTTP methods and status codes.
- Maintain consistent API response structures.
- Implement server-side pagination, filtering, and sorting.
- Validate all incoming requests.
- Implement proper authentication and authorization.
- Document important APIs and their expected behavior.

9. SECURITY
- Follow OWASP security recommendations.
- Implement role-based access control.
- Protect sensitive transporter, driver, and operational information.
- Validate and sanitize all untrusted input.
- Prevent SQL injection, XSS, CSRF, and unauthorized access.
- Never expose credentials, secrets, or sensitive information.
- Apply least-privilege access principles.

10. PERFORMANCE AND SCALABILITY
- Design for increasing loading records and operational users.
- Optimize database queries and API responses.
- Use pagination for large datasets.
- Implement caching only where appropriate.
- Avoid unnecessary API requests and frontend rendering.
- Monitor performance bottlenecks.

11. TESTING AND QUALITY ASSURANCE
- Write unit, integration, and feature tests where appropriate.
- Test all important loading workflows.
- Test role permissions and authorization.
- Validate status transitions and assignment conflicts.
- Test edge cases, invalid inputs, and failure scenarios.
- Verify existing functionality after changes.
- Do not consider a feature complete without testing.

12. LOGGING AND AUDITABILITY
- Maintain traceability for important business operations.
- Record who performed important actions and when.
- Track relevant changes to loading requirements and assignments.
- Avoid logging passwords, tokens, or sensitive personal information.
- Use structured and searchable logs.

13. CODE QUALITY AND MAINTAINABILITY
- Follow established project coding conventions.
- Write readable, reusable, and self-documenting code.
- Avoid unnecessary dependencies.
- Use meaningful variable, function, and component names.
- Keep functions focused and maintainable.
- Refactor responsibly without breaking existing functionality.

14. INTEGRATION AND COMPATIBILITY
- Investigate existing TruckMitr APIs and integrations before connecting them.
- Reuse existing services and business logic where appropriate.
- Maintain compatibility with existing TruckMitr systems.
- Never assume an API endpoint or integration exists.
- Handle external service failures gracefully.

15. DEVELOPMENT WORKFLOW AND GOVERNANCE
- Inspect existing implementation before modifying code.
- Understand requirements before planning implementation.
- Follow Spec-Driven Development.
- Define requirements, technical plans, and tasks before implementation.
- Identify dependencies and risks before making changes.
- Never make unnecessary changes to unrelated modules.
- Verify all changes before marking tasks complete.
- Update documentation when architecture or workflows change.

CONSTITUTION GOVERNANCE:
- Establish clear, measurable, and enforceable principles.
- Include rationale and compliance requirements for important principles.
- Identify principles that must be followed in every feature.
- Define how deviations should be documented and approved.
- Ensure all future specifications, plans, tasks, and implementations follow this Constitution.

FINAL REQUIREMENT:
Generate the Constitution in the official Spec Kit format at:

.specify/memory/constitution.md

Use professional technical language.
Avoid generic, vague, repetitive, or unnecessarily restrictive rules.

The Constitution must serve as the long-term engineering governance document for the TruckMitr Loading Module.















"""