# PC_Builder
The PC Builder Web Application is a web-based platform that allows users to create and manage custom computer configurations by selecting different hardware components. The application provides an organized way to browse components, group them into PC builds, and view detailed information for each build and component.

-Project Goals:

Build a real-world Django web application
Practice database relationships (One-to-Many, Many-to-Many)
Work with Django FBVs and CBVs
Implement full CRUD operations
Use Django Forms with validation
Apply template inheritance and Bootstrap styling
Follow best practices for project structure and version control

-Application Structure:

1️⃣ components
Manages all hardware components.

  Models:

  Component
  Category
  Tag

  Relationships:

  Component → Category (Many-to-One)
  Component ↔ Tag (Many-to-Many)

  Features:

  Component list, detail, create, edit, delete
  Form validation with help texts and error messages

2️⃣ builds
Manages PC configurations (builds).

  Models:

  PCBuild

  Relationships:

  PCBuild ↔ Component (Many-to-Many)

  Features:

  Create PC builds by selecting multiple components
  View build details and availability status
  CRUD functionality for builds

3️⃣ common
Provides shared functionality and static pages.

  Includes:

  Home page
  About page
  Base template
  Custom 404 error page
  Global navigation and footer

-Database Design:
Minimum of 3 models

  Includes:

  Many-to-One relationship
  Many-to-Many relationship
  Uses Django ORM with relational integrity

-Technologies Used:

  Python
  Django
  PostgreSQL
  HTML5
  Bootstrap 5
  GitHub

Developed by Simeon Kachulski
Django Web Development Student
