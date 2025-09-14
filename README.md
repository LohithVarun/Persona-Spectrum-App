# Persona Spectrum

Persona Spectrum is a mobile personality assessment app designed to provide users with deep insights into their character. The application uses a structured, 30-item psychometric questionnaire where users rate their responses on a five-point scale. A Python backend, built with the FastAPI framework, processes these answers using a deterministic weighting algorithm to score the user across four core personality dimensions (Energy, Information, Decisions, and Lifestyle). The system utilizes a SQLite database for data persistence, with results and recommendations structured in JSON and mapped to Kotlin data classes in the Android application. Based on the scores, the app generates a detailed personality profile and delivers a personalized development plan with actionable advice and relevant app suggestions to foster personal growth.

## Problem Statement

In a world saturated with self-assessment tools, many individuals find existing personality apps to be either overly simplistic and unscientific, providing little more than superficial entertainment, or excessively dense and academic, leaving them with complex data but no clear path for self-improvement. Users often struggle with generic, one-size-fits-all advice that fails to resonate with their personal context or provide actionable steps. This leads to a frustrating cycle of seeking self-knowledge but ending up with either shallow labels or unactionable analysis. Persona Spectrum directly tackles this gap by creating a focused, scientifically-grounded experience that is both insightful and practical. By combining a structured psychometric assessment with a powerful backend, our app moves beyond simple categorization to deliver a personalized development plan. We provide users not just with an understanding of *who* they are, but with concrete, tailored recommendations and resource suggestions, empowering them to actively and intelligently pursue their personal and professional growth.

## My Role

The goal of this project was to design and build a full-stack personality assessment application that provides users with a clear and actionable understanding of their character. The system works by having a native Android client communicate with a backend API. Users complete a structured psychometric questionnaire on the app, and the backend service analyzes their responses to generate a detailed personality profile. The application then presents this profile along with a personalized development plan, complete with tailored advice and resources to guide the user's personal growth.

## My Responsibility

*   **Full-Stack Architecture Design:** Planned the complete system architecture, defining the relationship between the Python backend, the Android frontend, and the database.
*   **Backend API Programming:** Developed the server-side application using Python and FastAPI to manage all business logic, including user accounts, assessment scoring, and recommendation generation.
*   **Database Implementation:** Designed and managed the SQLite database with SQLAlchemy, creating the schemas and logic for all data persistence.
*   **Android App Development:** Built the native mobile application in Kotlin, programming all activities, user flows, and state management from scratch.
*   **User Interface Construction:** Translated Figma designs into responsive XML layouts, ensuring the mobile interface was functional, intuitive, and matched the visual prototype.
*   **System Integration and Networking:** Implemented and configured the Retrofit library in the Android app to handle all API calls for seamless data exchange with the backend.
*   **Iterative Refinement and Debugging:** Systematically tested the application, identified bugs across the full stack, and implemented fixes to improve functionality and align with project goals.
