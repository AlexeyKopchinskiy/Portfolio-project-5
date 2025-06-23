# Portfolio-project-5
Portfolio Project 5 - E-commerce Applications

# 📝 InkWell – A Premium Blogging Platform

**InkWell** is a full-stack blogging platform that allows authors to publish both public and subscriber-only posts. It includes e-commerce integration for subscriptions, secure role-based authentication, SEO features, and a clean, accessible UI.

## 📌 Table of Contents
- [Project Overview](#project-overview)
- [User Types & User Stories](#user-types--user-stories)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Agile Workflow](#agile-workflow)
- [Wireframes & UX Design](#wireframes--ux-design)
- [Setup Instructions](#setup-instructions)
- [Testing](#testing)
- [Deployment](#deployment)
- [License](#license)

## How to View the Project
- [View the deployed website](https://github.com/AlexeyKopchinskiy/Portfolio-project-5/)

## 📖 Project Overview

This platform allows authors to manage and monetize content while providing a premium experience for paid subscribers. The goal is to provide a clean, SEO-optimized, and secure blogging space with real e-commerce functionality.

## 👥 User Types & User Stories

### Site Owner
- Manage posts, categories, and publishing schedule
- Track subscribers and view platform analytics
- Receive notifications of new subscriptions and comments

### Visitor / Reader
- Browse and read public blog posts without registration
- Register, log in, and subscribe for premium content
- Like, bookmark, and comment on posts

Check out the full list of [user stories and issues here](#) ← *(you can link to your Issues tab or GitHub project board)*

## ✨ Features

- Stripe-powered subscriptions
- Public and premium post access
- Role-based authentication
- Responsive, accessible UI with dark/light mode
- Bookmarking, commenting, and category filters
- Facebook product page / promotional mockup
- Newsletter signup and SEO features (meta tags, sitemap)

## 🛠 Technologies & Software Used

---------------------------------------------
| Purpose            | Tool                 |
|--------------------|--------------------- |
| Code Development   | Visual Studio Code   |
| Backend Framework  | Django (Python)      |
| Database           | PostgreSQL           |
| UI Styling         | HTML, CSS, Bootstrap |
| Design/Mockups     | CorelDraw, Photoshop |
| Wireframing        | CorelDraw, Photoshop |
| Deployment         | Heroku (or other)    |
| Payments           | Stripe API           |
| Version Control    | Git & GitHub         |
---------------------------------------------

## 🚀 Agile Workflow

- Agile board managed with GitHub Issues and Milestones  
- User stories split into:
  - Developer stories
  - Site owner stories
  - Visitor stories
- Labels include `Must-Have`, `Should-Have`, and `Could-Have`
- Milestones:
  - Project Setup
  - Auth & Roles
  - E-Commerce
  - Blog Engine
  - UX/UI
  - SEO & Marketing
  - Testing & Deployment

## 📐 Wireframes & UX Design

- Homepage  
- Post detail & premium prompt  
- Admin dashboard  
- User profile + saved posts  

### Website muck ups

#### 🏠 Homepage (Public View)

+----------------------------------------------------------+
| LOGO         | Home | Blog | Subscribe | Log In/Out      |
+----------------------------------------------------------+
| [Hero Banner: "Discover Powerful Writing"]               |
| [CTA Button: Subscribe for Premium Content]              |
+----------------------------------------------------------+
| [Filter: All | Fiction | Finance | Health | ... ]        |
+----------------------------------------------------------+
| [Post Thumbnail]  [Post Title]  [Excerpt...] [Read More] |
| [Post Thumbnail]  [Post Title]  [Excerpt...] [Read More] |
| [Post Thumbnail]  [Post Title]  [Excerpt...] [Read More] |
+----------------------------------------------------------+
| Newsletter Signup | About | License Info | Social Links  |
+----------------------------------------------------------+


#### 📄 Post Detail (Premium Gate Example)


+----------------------------------------------------------+
| LOGO | Home | Blog | My Account | Log Out                |
+----------------------------------------------------------+
| [Post Title: e.g. "How I Found My Voice Writing Daily"]  |
| Author: Alexey • Date • Tags: Fiction, Journaling        |
+----------------------------------------------------------+
| [Cover Image or Large Visual]                            |
+----------------------------------------------------------+
| You’ve hit premium content! 🔒                           |
| This post is for subscribers only.                       |
| [Subscribe to Unlock Full Post]                          |
| [Login as a Subscriber]                                  |
+----------------------------------------------------------+
| Already a subscriber? Welcome back. Content loads here ↓ |
+----------------------------------------------------------+
| [Like] [Bookmark] [Share]                                |
+----------------------------------------------------------+


#### 🔐 Login / Register


+-------------------------------+
|       Welcome Back! 🔐       |
+-------------------------------+
| [ Email ]                     |
| [ Password ]                  |
| [Log In]                      |
| [Forgot Password?]            |
+-------------------------------+
| New here? [Create an Account] |
+-------------------------------+


#### 🧑‍💼 Admin Dashboard (Site Owner View)

+--------------------------------+
| Sidebar:                       |
| - Dashboard                    |
| - Posts                        |
| - Subscribers                  |
| - Analytics                    |
| - Settings                     |
+--------------------------------+
|         Recent Activity        |
| [New post created]             |
| [3 new subscribers today]      |
+--------------------------------+
|           Posts Table          |
| Title      | Status | Edit | 🗑 |
| "Post A"   | Draft  | ✏️   | x |
| "Post B"   | Live   | ✏️   | x |
+--------------------------------+
| [+ New Post] [Export Data]     |
+--------------------------------+


#### 💳 Subscription Page


+--------------------------------------------------+
| Choose Your Plan 💼                              |
+--------------------------------------------------+
| 🟦 Monthly - $5/month                            |
| - Access premium posts                           |
| - Newsletter                                     |
| [Subscribe]                                      |
+--------------------------------------------------+
| 🟥 Yearly - $50/year (save 20%)                 |
| - All Monthly features                           |
| - Bonus e-book                                   |
| [Subscribe]                                      |
+--------------------------------------------------+
| [Secure Stripe Checkout Form Here]               |
| Card Info • Billing Email • Pay Now              |
+--------------------------------------------------+
| [Return to Blog]                                 |
+--------------------------------------------------+

### Wireframe design

#### Homepage

![Homepage wireframe](/static/images/pp5-wireframe-startpage.png)

#### Mobile Homepage

![Homepage wireframe mobile ](/static/images/PP5-wireframe-mobile-homepage.png)

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/inkwell.git
cd inkwell
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## ✅ Testing
- Manual testing checklist available in the /testing folder
- Unit and integration tests written using Django’s TestCase framework
- Accessibility and SEO audited with Lighthouse

## 🚢 Deployment
- Live app hosted on Heroku (or insert platform)
- Environment variables managed securely via .env files
- DEBUG = False and secret keys hidden in production

## 📄 License
🧑‍💻 Code
This project is licensed under the MIT License.

## ✍️ Content
All original written content (blog posts, mock posts, text) is licensed under
Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).

## 🙌 Acknowledgements
Special thanks to the tutors, the assessment handbook, and caffeine.