#  Stackportfol.io

You can view the live site at [https://stackportfol.io](https://stackportfol.io).

![Stackportfol.io](./documentation/stackportfolio.png)

Stackportfol.io is a platform that allows Developers to add showcase their projects and associate them with the skills that they used to create them. Since the skills are linked to projects, Recruiters have peace of mind that the Developers they are contacting have the skills that they say they have.

## Table of Contents

- [Planning and Design](#planning-and-design)
  - [Site objective](#site-objective)
  - [Opportunities](#opportunities)
  - [Scope](#scope)
  - [User stories and Epics](#user-stories-and-epics)
    - [Account management](#account-management)
    - [User profiles](#user-profiles)
    - [Project management](#project-management)
    - [Job post management](#job-post-management)
    - [Technology management](#technology-management)
    - [Miscellaneous](#miscellaneous)
  - [Wireframes](#wireframes)
  - [Colours and Fonts](#colours-and-fonts)
    - [Colours](#colours)
    - [Fonts](#fonts)
  - [User flowchart](#user-flowchart)
- [Development](#development)
  - [Site Features](#site-features)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
- [Deployment](#deployment)
  - [ElephantSQL Database](#elephantsql-database)
  - [Cloudinary API](#cloudinary-api)
  - [Heroku Deployment](#heroku-deployment)
  - [Local Deployment](#local-deployment)
    - [Cloning](#cloning)
    - [Forking](#forking)
- [Future Features](#future-features)
- [Testing and Agile Notes](#testing-and-agile-notes)
  - [Testing](#testing-documentation)
  - [Agile](#agile-notes)
- [Technologies used](#technologies-used)
- [Credits](#credits)
  - [Resources](#resources-used)
  - [Acknowledgements](#acknowledgements)

## Planning and Design

###  Site objective

While Developers can use a site such as LinkedIn to add projects, the architecture is set to serve the needs of a number of different job functions. Due to the fact that the site us not focused on Developers, the project showcase lacks many features that Developers need. Recruiters who are searching for Developers for role lack the evidence that a Developer has the skills for which they are searching. In many cases, a skill might be added to a professional profile just because someone has heard or watched a video about it.

Stackportfol.io allows Developers to showcase their projects, which then allows Recruiters to find Developers who have proven skills for their job postings. It's a win-win for both parties.

###  Opportunities

Being a Developer myself, I have a lot of feature ideas for the Stackportfol.io platform. I have listed them in the table below, rating them by their importance and difficulty. The rating system is based on the MoSCoW method of prioritisation.

| Feature                         | Importance | Difficulty | Project priority |
| ------------------------------- | ---------- | ---------- | ---------------- |
| **Account Features**            |            |            |                  |
| Account creation                | 5          | 3          | Must have        |
| Account login                   | 5          | 3          | Must have        |
| Account logout                  | 5          | 3          | Must have        |
| Account deletion                | 5          | 2          | Must have        |
| Account update                  | 5          | 3          | Must have        |
| Account preferences             | 3          | 4          | Could have       |
| Social login/registration       | 3          | 4          | Could have       |
| **User Features**               |            |            |                  |
| User profiles                   | 5          | 3          | Must have        |
| User profile search             | 3          | 4          | Could have       |
| User messaging system           | 1          | 5          | Won't have       |
| User notifications              | 1          | 5          | Won't have       |
| User activity feed              | 1          | 5          | Won't have       |
| Tech user unique profile URL    | 4          | 3          | Should have      |
| Job seeking types               | 1          | 4          | Won't have       |
| **Project Features**            |            |            |                  |
| Project creation                | 5          | 3          | Must have        |
| Project update                  | 5          | 3          | Must have        |
| Project deletion                | 5          | 3          | Must have        |
| Project search                  | 3          | 4          | Could have       |
| Project tech association        | 5          | 4          | Must have        |
| Project Contributors            | 3          | 5          | Won't have       |
| Project commenting              | 2          | 5          | Won't have       |
| Report job post/project         | 2          | 5          | Won't have       |
| Project/Job post bookmarking    | 2          | 5          | Won't have       |
| **Job Features**                |            |            |                  |
| Job creation                    | 5          | 3          | Must have        |
| Job update                      | 5          | 3          | Must have        |
| Job deletion                    | 5          | 3          | Must have        |
| Job search                      | 2          | 4          | Could have       |
| Job list                        | 4          | 3          | Should have      |
| Job post tech                   | 5          | 3          | Must have        |
| Job remote/on-site/hybrid       | 4          | 2          | Should have      |
| Job post benefits               | 2          | 4          | Won't have       |
| Job post salary                 | 3          | 2          | Should have      |
| Job post application            | 2          | 5          | Won't have       |
| Associate company with job post | 1          | 4          | Won't have       |
| **Tech Features**               |            |            |                  |
| Tech search                     | 3          | 4          | Could have       |
| Tech Aliases                    | 2          | 4          | Won't have       |
| Tech position                   | 1          | 2          | Could have       |
| **Miscellaneous Features**      |            |            |                  |
| Skills for user and project     | 2          | 5          | Won't have       |
| Company creation                | 1          | 5          | Won't have       |
| Expected UI/UX                  | 5          | 2          | Must have        |

<details>
  <summary>Click here to expand the priority descriptions and percentages</summary>

| Priority    | Percentage                | Description                                                                                                                                                            |
| ----------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Must have   | 60%                       | These are the features that are essential for the site to be usable. If any of these features are missing, the site will not be usable.                                |
| Should have | 16%                       | These are the features that are important, but not essential. If any of these features are missing, the site will still be usable.                                     |
| Could have  | 24%                       | These are the features that are nice to have, but not essential. If any of these features are missing, the site will still be usable.                                  |
| Won't have  | Excluded from calculation | These are the features that are not essential and will not be implemented in the current project. If any of these features are missing, the site will still be usable. |

</details>

### Scope

Since there are a quite a few features that I would like to implement, I have decided to focus on the core features of the site. The core features are the features that are essential for the site to be usable. The core features are:

- Account management
  - Account creation, updating, and deletion
  - Account login and logout
- User profiles
  - User profiles are created when an account is created
  - User profiles can be updated and deleted
- Project management
  - Projects can be created, updated, and deleted
  - Projects can be associated with a tech user
- Technology management
  - Technologies can be created, but only the Admin should be able to update and delete them
  - Multiple technologies can be associated with a project/job post
- Job post management
  - Job posts can be created, updated, and deleted
  - Job posts can be associated with a recruiter user

Apart from the above, there is also the more general user story of the expected User Experience and User Interface of the site, which I have also included in the scope.

There is also a few features that use search, but I don't feel the functionality is fully required for the Minimum Viable Product (MVP). I have marked many of them as could have and will added user stories to address if time permits near the end of the project.

### User stories and Epics

I have created Epics for each of the core features mentioned in my scope. Here are the planned user stories within each one:

#### Account management

- As a **user**, I can **create an account** so that I can **have my preferences saved**.
- As a **user**, I can **update my personal details** so that I can **ensure my data is accurate and displayed correctly**.
- As a **user**, I can **delete my account** so that I can **have peace of mind that my data is no longer being retained unnecessarily**.
- As a **user**, I can **sign up as a tech user or a recruiter** so that I can **use the platform based on my role**.
- As a **user**, I can **log out of my account** so that I can **feel secure when not using my account**.
- As a **user**, I can **choose update by account preferences** so that I can **have more control into how my profile is view and what information is shared**.
- As a **tech user**, I can **do sign up or log in using a social account** so that I can **easily signup and have my details prepopulated**.

#### User profiles

- As a **user**, I can **have a profile page** so that I can **display my details and projects/jobs**.
- As a **user**, I can **create a unique profile URL** so that I can **easily share my profile with others**.
- As a **user**, I can **search user profiles** so that I can **find friends, colleagues or potential candidates to connect with**.

#### Project management

- As a **tech user**, I can **create a project** so that I can **display it in my portfolio**.
- As a **tech user**, I can **update my project details** so that I can **keep my project relevant to views**.
- As a **tech user**, I can **delete a project** so that I can **keep focus on my most relevant projects**.
- As a **user**, I can **add different technologies to my job posts, projects or profile (tech user)** so that I can **use them for postings or to be associated with those skills**.
- As a **user**, I can **search for projects** so that I can **find a project relevant to my interest or job post**.

#### Job post management

- As a **recruiter user**, I can **create a job post** so that I can **to attract the attention of potential applicants**.
- As a **recruiter user**, I can **update the details of my job post** so that I can **ensure the most up-to-date information about the post is provided**.
- As a **recruiter user**, I can **delete a job post** so that I can **remove out-of-date posts**.
- As a **recruiter user**, I can **specify the job location type** so that I can **ensure only those who match the job location, such as on-site, hybrid or remote show interest in the job**.
- As a **user**, I can **see a job position's salary range** so that I can **decide whether to apply or not**.
- As a **user**, I can **view a list of created job posts** so that I can **view open positions**.
- As a **user**, I can **search jobs** so that I can **find the most relevant job to me**.

#### Technology management

- As a **user**, I can **search for specific technologies such as a 404 page** so that I can **see associated job posts or projects with those technologies**.

#### Miscellaneous

- As a **user**, I can **see pages that I expect on a website** so that I can **have a familiar user experience**.
- As an **admin**, I can **have a good user interface and experience, including different filters or functions** so that I can **easily manage different data effectively**.

###  Wireframes

I have created wireframes for the main pages of the site. I have used [Balsamique](https://balsamiq.com/) to create the wireframes. Here are the wireframes for the main pages:

<details>
  <summary>Homepage - Desktop (click to expand)</summary>

![Homepage - Desktop](./documentation/wireframes/homepage-desktop.png)

</details>

<details>
  <summary>Homepage - Mobile (click to expand)</summary>

![Homepage - Mobile](./documentation/wireframes/homepage-mobile.png)

</details>
<br>
<details>
  <summary>Forms - Desktop (click to expand)</summary>

![Sign up page - Desktop](./documentation/wireframes/sign-up-desktop.png)

</details>

<details>
  <summary>Forms - Mobile (click to expand)</summary>

![Sign up page - Mobile](./documentation/wireframes/sign-up-mobile.png)

</details>

<br>
<details>
  <summary>Tech user profile - Desktop (click to expand)</summary>

![Tech user profile - Desktop](./documentation/wireframes/tech-user-profile-desktop.png)

</details>

<details>
  <summary>Tech user profile - Mobile (click to expand)</summary>

![Tech user profile - Mobile](./documentation/wireframes/tech-user-profile-mobile.png)

</details>

<br>

<details>
  <summary>Project List Page - Desktop (click to expand)</summary>

![Project List Page - Desktop](./documentation/wireframes/project-list-mosaic-desktop.png)

</details>

<details>
  <summary>Project List Page - Mobile (click to expand)</summary>

![Project List Page - Mobile](./documentation/wireframes/project-list-mosaic-mobile.png)

</details>

<br>

<details>
  <summary>Project Page - Desktop (click to expand)</summary>

![Project Page - Desktop](./documentation/wireframes/project-page-desktop.png)

</details>

<details>
  <summary>Project Page - Mobile (click to expand)</summary>

![Project Page - Mobile](./documentation/wireframes/project-page-mobile.png)

</details>

<br>
<details>
  <summary>Recruiter user profile - Desktop (click to expand)</summary>

![Recruiter user profile - Desktop](./documentation/wireframes/recruiter-profile-desktop.png)

</details>

<details>
  <summary>Recruiter user profile - Mobile (click to expand)</summary>

![Recruiter user profile - Mobile](./documentation/wireframes/recruiter-profile-mobile.png)

</details>

<br>

<details>
  <summary>Job Board - Desktop (click to expand)</summary>

![Job Board - Desktop](./documentation/wireframes/job-board-desktop.png)

</details>

<details>
  <summary>Job Board - Mobile (click to expand)</summary>

![Job Board - Mobile](./documentation/wireframes/job-board-mobile.png)

</details>

<br>

<details>
  <summary>Job Page - Desktop (click to expand)</summary>

![Job Page - Desktop](./documentation/wireframes/job-page-desktop.png)

</details>

<details>
  <summary>Job Page - Mobile (click to expand)</summary>

![Job Page - Mobile](./documentation/wireframes/job-page-mobile.png)

</details>

<br>

<details>
  <summary>Search - Desktop (click to expand)</summary>

![Search - Desktop](./documentation/wireframes/search-desktop.png)

</details>

<details>
  <summary>Search - Mobile (click to expand)</summary>

![Search - Mobile](./documentation/wireframes/search-mobile.png)

</details>

### Colours and Fonts

#### Colours

The colours used on the site are:

[#0166ff] (Primary)
[#333333] (Base text)
[#fff7ff] (Base background and light text)
[#eff7ff] (Accent background)
[#131e32] (Dark background)

Here is a screenshot of the palette from Cooolors:

![Colour palette](./documentation/stackportfolio-palette.png)

#### Fonts

Here is a screenshot of the fonts I intended to use on the site:

![Fonts](./documentation/stackportfolio-fonts.png)

After using Tailwind, I realised that I liked the body font from Tailwind more, so I ended up leaving that instead. The headings still use my originally intended font.

### User flowchart

The user flowchart was created using [Draw.io](https://app.diagrams.net/). The flowchart shows the different paths that a user can take through the site.

![User flowchart](./documentation/diagrams/user-flowchart.png)

## Development

### Site Features

The site has a number of standard features, plus some which are specific features that are important for the site's purpose. The site us fully responsive and has been tested on Firefox, Safari and Google Chrome. Here is a list of the features on the site, along with screenshots:

- **Header**
  - The header is a standard header and is responsive so that the menu is collapsed into a hamburger toggle on mobile. I would also like to make this a sticky header in future, but I haven't implemented that yet.

![Header](./documentation/features/header.png)

- **Hompeage hero section**
  - The hero section provides a tagline for the site and a sign up call-to-action button and link for developers and recruiters. When logged in, the links change so that it redirects the user to their profile instead.

![Homepage hero section](./documentation/features/hero-section.png)

- **Homepage featured projects slider**
  - The featured slider selects 6 projects randomly and displays them on the homepage. The user can go through the projects and click on the project to go to the project page. There is also a call-to-action button for the user to go to the projects list page.

![Homepage featured projects slider](./documentation/features/featured-projects-slider.png)

- **Footer**
  - The final footer is much more minimalistic than my original wireframe. I decided to not add anything that would distract from the primary purpose of the site. I only have one column of links, which lead to the **About** and **Careers** pages. The **Careers** page is a placeholder for now, but I plan to add a page that lists the current job openings at Stackportfol.io. It currently still allows for the user to email `contact@stackportfol.io` so that expression of interest can be received. In future, I plan to add more items to the footer.

![Footer](./documentation/features/footer.png)

- **Account type**
  - The Account type page allows the user to choose whether they are signing up as a tech user or a recruiter. Tech users can also sign up using GitHub, but recruiters may only sign up using the standard form.

![Signup type](./documentation/features/signup-type.png)

- **Tech signup - Details**
  - The tech signup form is for tech users (developer, testers, etc.) to sign up. The details page collects the user's first name, last name, username, email and password. The username and email must be unique - I validate this server side, so it doesn't do any async call to check if the user already exists, but I hope to add that in the future. This page asks for the same details on the recruiter signup form.

![Tech signup - Details](./documentation/features/tech-user-signup-details.png)

- **Tech signup - Profile**
  - The profile page collects the user's profile image, bio, location, and website. The user can leave any of these details blank and still complete the signup. This step differs from a recruiter signup as it also asks for a GitHub username, their work location preference and if the user is currently looking for work.

![Tech signup - Profile](./documentation/features/tech-user-signup-profile.png)

- **Tech signup - Summary**
  - The summary page shows the user a summary of the details they have entered. The user can go back to the previous pages to edit the details if they wish. The user can also submit the form to create their account.

![Tech signup - Summary](./documentation/features/signup-summary.png)

- **Recruiter signup**
  - The recruiter signup is pretty similar to the tech user signup, but it doesn't have as many profile fields. For this reason, this is screenshot is just to show the fact there is a different form.

![Recruiter signup](./documentation/features/recruiter-signup.png)

- **Form validation**
  - There is frontend validation on forms that require it. In this example, I am using the signup form, but other forms on the site also have validation. The validation is also done server side, so that if the user bypasses the frontend validation, the form will still be validated.

![Form validation](./documentation/features/form-validation.png)

- **Sign in page**
  - The sign in page allows the user to sign in using their username or email and password. The user can also click on the link to go to the sign up page. If it is a tech user, they can also use GitHub to log in. If the email is already in use, it will associate that GitHub account with the existing account. If it doesn't exist, it will create a new account and use the GitHub credentials.

![Sign in page](./documentation/features/sign-in-page.png)

- **User Search**
  - The search page allows the user to search using a query, which searches the user's name. The user can also filter users by their tech skills, whether they have the tech listed or if they have the specific combination of tech queried.

![User Search](./documentation/features/user-search.png)

- **Project Search**
  - The project search searches projects by their titles or descriptions. Like with the user search, the user can also filter by tech skills. Only active projects are shown in the search results.

![Project Search](./documentation/features/projects-search.png)

- **Job Post Search**
  - Like the project search, job posts are searched by title or description. The user can also filter by tech skills, but in this case, it will be the required tech skills. Only active job posts are shown in the search results.

![Job Post Search](./documentation/features/job-post-search.png)

- **Search include tech**
  - The include tech functionality allows users to search for any user, project or job post, which contain any of the tech listed.

![Search include tech](./documentation/features/search-include-tech.png)

- **Search match tech**
  - The match tech functionality allows users to search for any user, project or job post, which contain all of the tech listed.

![Search match tech](./documentation/features/search-match-tech.png)

- **Project list**
  - The project list page shows all the projects on the site, with the most recent project shown first. The project page is also paginated so that a max of 9 projects are shown for performance reasons. The user can click on the project to go to the project's detail page.

![Project list](./documentation/features/projects-list.png)

- **Project detail**
  - The project detail page shows the project's details, including the project's title, description, tech and creator. If the user is the creator of the project, they can also edit or delete the project.

![Project detail](./documentation/features/project-detail-page.png)

- **Job Posts list**
  - Like the projects list, the jobs list shows all the jobs on the site, with the most recent job shown first. The jobs are also paginated so that a max of 9 jobs are shown for performance reasons. The user can click on the job to go to the job's detail page.

![Jobs list](./documentation/features/job-posts-list.png)

- **Job detail**
  - The job detail page shows the job's details, including the job's title, description, tech and creator. If the user is the creator of the job, they can also edit or delete the job. The job detail page also has a side panel with the poster's details, so they can easily be found or contacted. Job posts can only be posted by users with a recruiter profile, but for the sake of demonstration, my user has both a tech and recruiter profile. For this reason, the poster details in the screenshot has my tech user details, but this would normally be a recruiter's details.

![Job detail](./documentation/features/job-post-detail-page.png)

- **Tech user profile**
  - The tech user profile shows the user's details, including their profile image, bio, location, website, GitHub username, work location preference and if they are looking for work. We can also see the user's projects and the tech that they have listed on their profile. If the user is the owner of the profile, they can also edit or delete the profile. The "Add project" button will also only show for the profile owner. To edit the account settings (such as the email or username), the user must access it from the dropdown menu.

![Tech user profile](./documentation/features/tech-user-profile.png)

- **Recruiter user profile**
  - The recruiter user profile shows the user's details, including their profile image, bio, location and company. We can also see the user's job posts. If the user is the owner of the profile, they can also edit or delete the profile. The "Add job post" button will also only show for the profile owner.

![Recruiter user profile](./documentation/features/recruiter-user-profile.png)

- **Edit profile**
  - If the user owns a profile, they can access the **Edit profile** page. This page contains the optional details of the profile, such as profile image, location or telephone number.

![Edit profile](./documentation/features/edit-profile.png)

- **Edit account settings**
  - The account settings page allows the user to change their username, email or name. The user currently cannot update their password, but it is a feature that will be added in the future. When the username is updated, it also updates the user's profile URL (slug).

![Edit account settings](./documentation/features/account-settings-edit.png)

- **Confirmation modal**
  - When a user opts to delete their profile, project or job post, there is a modal popup to confirm that they want to delete the item. This is to prevent accidental deletion. Since this also causes a cascade deletion of projects or job posts, I would also like to include more information on the repercussions in the future.

![Confirmation modal](./documentation/features/confirmation-modal.png)

- **Create Project Form**
  - The create project form is only accessible to users with a tech user profile. They can add the project's title, description, the deployed link, the GitHub repo link, featured image and any tech used on the project. They can also either set it to active or draft. If it is set to draft, it will not be shown on the project list or search.

![Create Project Form](./documentation/features/create-project-form.png)

- **Edit Project Form**
  - The edit project form is only accessible to users with a tech user profile. They can update the same details as the create project form, but also have the current featured image displayed. They can either clear or update the featured image.

![Edit Project Form](./documentation/features/project-edit.png)

- **Inactive project**

  - If a job post or project is set to inactive, it will not show up on the search or project list. However, if a user owns the project or job post, they will see it listed with an "Inactive" badge. This way, they can still access it to edit or delete it.

![Inactive project](./documentation/features/inactive-project.png)

- **Associated tech**
  - On projects and job posts, the user can add the associated tech. The tech can be added the name and then clicking on the dropdown, or by pressing enter. If the tech is already approved on the backend, the tech badge shows up with the site's primary colour. If is not approved, it will still be added, but show up with the site's secondary colour and have a tooltip showing that it is pending admin approval. Approved tech that is added to a project is automatically added to a user's profile. The user can also remove the tech by clicking on the tech.

![Associated tech](./documentation/features/associated-tech.png)

- **Create Job Post Form**
  - The create job post form is only accessible to users with a recruiter user profile. They can add the job's title, description, the job's location type, the job's salary range, the location work type, the job's tech requirements and the company. They can also either set it to active or draft. If it is set to draft, it will not be shown on the job list or search.

![Create Job Post Form](./documentation/features/create-job-post-form.png)

- **Edit Job Post Form**
  - The edit job post form is only accessible to users with a recruiter user profile. They can update the same details as the create job post form.

![Edit Job Post Form](./documentation/features/edit-job-post.png)

- **Domain and SSL**
  - The site is hosted on Render, which provides a free SSL certificate. The site is also hosted on a custom domain, which is `https://stackportfol.io`.

![Domain and SSL](./documentation/features/domain-and-ssl.png)

### Entity Relationship Diagram

The Entity Relationship Diagram (ERD) was created using [Draw.io](https://app.diagrams.net/). The ERD is a visual representation of the database structure. It shows the tables, the columns in each table, and the relationships between the tables. Here is the ERD from my planning:

![Entity Relationship Diagram](./documentation/diagrams/entity-relationship-diagram-third.png)

Here is the final ERD generated by using Graphviz and Django Extensions:

![Entity Relationship Diagram](./documentation/diagrams/erd.png)

<details>
  <summary>Click here to expand and see the first ERD draft</summary>

![Entity Relationship Diagram](./documentation/diagrams/entity-relationship-diagram-first.png)

</details>

<details>
  <summary>Click here to expand and see the second ERD draft</summary>

![Entity Relationship Diagram](./documentation/diagrams/entity-relationship-diagram-second.png)

</details>

### Technologies used

- [Django](https://www.djangoproject.com/)
  - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [JavaScript](https://www.javascript.com/)
  - JavaScript is a programming language that adds interactivity to your website.
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
  - Cascading Style Sheets (CSS) is a stylesheet language used to describe the presentation of a document written in HTML or XML.
- [HTML](https://html.spec.whatwg.org/)
  - HTML is the standard markup language for documents designed to be displayed in a web browser.
- [Python](https://www.python.org/)
  - Python is an interpreted, high-level and general-purpose programming language.
- [PostgreSQL](https://www.postgresql.org/)
  - PostgreSQL is a powerful, open source object-relational database system.
- [Cloudinary](https://cloudinary.com/)
  - Cloudinary is a cloud service that offers a solution to a web application's entire image management pipeline.
- [Heroku](https://www.heroku.com/)
  - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [Render](https://render.com/)
  - Render is a cloud platform that makes it easy for developers and teams to deploy and manage their applications and websites.
- [Tailwind CSS](https://tailwindcss.com/)
  - Tailwind CSS is a utility-first CSS framework for rapidly building custom user interfaces.
- [DaisyUI](https://daisyui.com/)
  - DaisyUI is a component library for Tailwind CSS.
- [Jest JS](https://jestjs.io/)
  - Jest is a JavaScript Testing Framework with a focus on simplicity.
- [UnitTest](https://docs.python.org/3/library/unittest.html)
  - The unittest comes standard with Python and is a testing framework.

As a way to "dogfood" the project, you can also see the project and it's technologies here: <https://www.stackportfol.io/user/stephendawson/project/stackportfolio>

## Deployment

The live deployed application can be found at [https://stackportfol.io](https://stackportfol.io), which is hosted on **Render**. I chose to host on **Render** as they provide a fully-free tier and a free SSL Certificate. However, the site can also be found at [https://stackportfolio-1340b88e89e7.herokuapp.com/](https://stackportfolio-1340b88e89e7.herokuapp.com/), which is hosted on **Heroku**. For simplicity, I will provide instructions on how to deploy to **Heroku**, since this is what many people are familiar with.

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database. ElephantSQL has previously offered the TinyTurtle plan, but it is being deprecated. In order to use it, you will first need to create an account and select it, but the below steps will be the same.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project, e.g. `stackportfolio`).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For _Primary interest_, you can choose _Programmable Media for image and video API_.
- Optional: _edit your assigned cloud name to something more memorable_.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key                     | Value                                                                |
| ----------------------- | -------------------------------------------------------------------- |
| `CLOUDINARY_URL`        | insert your own Cloudinary API key here                              |
| `DATABASE_URL`          | insert your own ElephantSQL database URL here                        |
| `DISABLE_COLLECTSTATIC` | 1 (_this is temporary, and can be removed for the final deployment_) |
| `SECRET_KEY`            | this can be any random secret key                                    |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `web: gunicorn app_name.wsgi > Procfile`
- _replace **app_name** with the name of your primary Django app name; the folder where settings.py is located_. In this case, that is `stackportfolio`.

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace _app_name_ with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the _requirements.txt_ file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "insert your own Cloudinary API key here")
os.environ.setdefault("DATABASE_URL", "insert your own ElephantSQL database URL here")
os.environ.setdefault("SECRET_KEY", "this can be any random secret key")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/stephendawsondev/stackportfolio)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/stephendawsondev/stackportfolio.git`

7. Press Enter to create your local clone.

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/stephendawsondev/stackportfolio)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Future Features

Any User stories that I was not able to fit into the scope of this project was added as a future feature. Since these features are dynamic (can either be added in the meantime or more can be added), you can [click here to go to the project board and see them in the Future Features column](https://github.com/users/stephendawsondev/projects/5/views/1?filterQuery=label%3A%22user+story%22). Broadly, I aim to first add features to attract Tech Users, then later to attract Recruiter Users.

## Testing and Agile notes

### Testing documentation

I documented all automated and manual tests in the [TESTING.md](./TESTING.md) file.

### Agile notes

I documented each Sprint and the notes on Agile in the [AGILE.md](./AGILE.md) file.

## Credits

### Resources Used

#### Project Management and GitHub Resources

- [Creating issue templates on GitHub](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)
- [GitHub Docs on issue templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates)
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)

#### Design and Wireframing

- [Balsamiq](https://balsamiq.com/)
- [Figma for designing the Favicon](https://www.figma.com/)
- [Draw.io](https://app.diagrams.net/)
- [ER 4 Inheritance video on Entity Relationship Diagrams](https://www.youtube.com/watch?v=ATgYkVTZBiI)
- [Database Design playlist by Caleb Curry](https://www.youtube.com/playlist?list=PL_c9BZzLwBRK0Pc28IdvPQizD2mJlgoID)
- [Graphviz for creating the ERD](https://graphviz.org/)
- [FontJoy for Font pairings](https://fontjoy.com/)
- [Cooolors for colour palette](https://coolors.co/)
- [Canva for creating image placeholders](https://www.canva.com/)
- [MoSCoW method - P3 Mastery](https://www.youtube.com/watch?v=j2Fpx1Yj9EQ)
- [Techsini](https://techsini.com/) for the mockup image used in my readme.

#### Database and ERD Tools

- [Django extensions for generating the ERD](https://django-extensions.readthedocs.io/en/latest/graph_models.html)
- [Pyparsing for generating the ERD](https://pypi.org/project/pyparsing/)

#### Development Tools, Libraries and Resources

- [Gunicorn documentation](https://docs.gunicorn.org/en/stable/)
- [dj_database_url](https://pypi.org/project/dj-database-url/0.4.2/)
- [Autopep8](https://pypi.org/project/autopep8/)
- [Django Allauth](https://docs.allauth.org/en/latest/)
- [Whitenoise](http://whitenoise.evans.io/en/stable/)
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/)
- [Pylint-Django for better linting](https://pypi.org/project/pylint-django/)
- [Widget Tweaks for styling allauth forms](https://pypi.org/project/django-widget-tweaks/)
- [Django documentation](https://docs.djangoproject.com/en/3.2/)
- [Documentation on extending allauth forms](https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/)
- [Slugify Django username](https://www.fullstackpython.com/django-utils-text-slugify-examples.html)
- [LoginRequiredMixin](https://docs.djangoproject.com/en/4.2/topics/auth/default/)
- [Django decorators](https://docs.djangoproject.com/en/4.2/topics/http/decorators/)
- [Django documentation on custom error pages](https://docs.djangoproject.com/en/3.2/topics/http/views/#customizing-error-views)
- [Django documentation on ManyToManyField](https://docs.djangoproject.com/en/3.2/ref/models/fields/#manytomanyfield)
- [Django docs on the radio widget](https://docs.djangoproject.com/en/4.2/ref/forms/widgets/#widgets-inheriting-from-the-select-widget)
- [Django docs on overriding delete for bulk methods](https://docs.djangoproject.com/en/4.2/topics/db/models/#overriding-model-methods)
- [Django documentation on the testing client](https://docs.djangoproject.com/en/4.2/topics/testing/tools/#the-test-client)
- [Django docs on messages levels for toasts](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/#message-levels)
- [Disabling intermediate logout step in allauth](https://stackoverflow.com/questions/18134807/how-to-disable-intermediate-signout-page-in-django-allauth)
- [LearnDjango tutorial on implementing Search](https://learndjango.com/tutorials/django-search-tutorial)
- [TailwindCSS Form Validation tutorial](https://dev.to/deyemiobaa/adding-custom-validation-to-a-form-with-tailwindcss-1e7d)
- [Stackoverflow post on populating objects in template](https://stackoverflow.com/questions/32389519/django-get-10-random-instances-from-a-queryset-and-order-them-into-a-new-querys)
- [MDN Article on the search element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
- [Reason to not convert my M2M tables to a through table](https://forum.djangoproject.com/t/changing-a-manytomanyfield-to-use-a-through-model/10581)
- [Stackoverflow post on custom replace filter](https://stackoverflow.com/questions/21483003/replacing-a-character-in-django-template)
- [Stackoverflow Post for fix on why some js files were not loading](https://stackoverflow.com/questions/64171461/collectstatic-whitenoise-cant-see-my-existing-file-on-deployment-to-heroku/64172052#64172052)
- [Issue with Tailwind Styles not applying to form elements on Stackoverflow](https://stackoverflow.com/questions/76729480/django-tailwind-styling-not-applied-to-template-variables-with-widget-attribut)

#### Styling and UI Components

- [Tailwind CSS](https://tailwindcss.com/)
- [DaisyUI Plugin](https://daisyui.com/)
- [Contact form component from Tailwind components](https://tailwindcomponents.com/component/basic-contact-form)
- [Tailwind Multiselect component from Tailwind Components](https://tailwindcomponents.com/component/multi-select)
- [Adapted carousel from Kindacode](https://www.kindacode.com/article/tailwind-css-create-an-image-carousel-slideshow/)
- [Heroicons](https://heroicons.com/)
- [404 Page template code from HyperUI Components](https://www.hyperui.dev/components/application-ui/error-pages#component-2)

#### Social Media and API Integration

- [Allauth docs about LinkedIn](https://docs.allauth.org/en/latest/socialaccount/providers/linkedin.html)
- [LinkedIn API docs](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/migration-faq?context=linkedin%2Fconsumer%2Fcontext)
- [Medium article on adding GitHub for social login using allauth](https://python.plainenglish.io/django-allauth-a-guide-to-enabling-social-logins-with-github-f820239fb73f)
- [Issue with AllAuth and LinkedIn](https://github.com/pennersr/django-allauth/issues/1641)
- [Social Account Adapter Documentation on AllAuth](https://docs.allauth.org/en/latest/socialaccount/configuration.html)

#### Testing resources

- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [Form Input Validity Docs on MDN](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState)
- [Geeks for Geeks docs for Python testing](https://www.geeksforgeeks.org/python-unittest-assertisnotnone-function/)
- [TestDriven.io on using the post_delete receiver](https://testdriven.io/tips/59a2752f-cdf3-4ba1-806d-15f29811037a/)
- [Ssali Jonathan playlist on test-driven development with Django](https://www.youtube.com/playlist?list=PLEt8Tae2spYlWWMN5azuYjvoItXDkQ1DQ)

#### Hosting and Deployment

- [Heroku](https://www.heroku.com/)
- [Render - used for hosting in the end](https://render.com/)
- [Cloudinary for asset hosting](https://cloudinary.com/)

### Acknowledgements

This was a tough project and there is still so much more I would love to add on in the future. I couldn't have gotten so much done without the feedback and advice from mentors, colleagues and friends. I would like to thank the following people for their help and support:

- My mentor, **[David Bowers](https://github.com/dnlbowers)** for his consistently great feedback. Each session I have had with him have been invaluable and I come away with a fresh perspective and ideas each time.
- My cohort lead [Alan Bushell](https://github.com/alan-bushell) who has provided some great support through the weekly cohort sessions, where he provided feedback on project ideas, and even thought up the name "Stackportfolio" on the spot when I told him what I was doing.
- My partner Tae who somehow managed to put up with me talking about this project for the past 2 months, as well as providing feedback on the design and user experience.
- My colleagues at [The Code Institute](https://codeinstitute.net/) who have provided some great feedback and support.
