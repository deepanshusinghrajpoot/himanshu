"""

Gathering Requirements
======================



Mythical Man-Month : decideing what i duild




Let build me a leaderboard for my game -> 8 words -> 100s systems

Architecture decisions changes - if requirement changes.


Boehm's Curv - Barry Boehm - Software Engineering Economics - 1981





1. Scope Clarification
----------------------

What users do and how?
    
     Use Cases -------------- Actions
     Goals ---------------- Must Do
     Non-Goals -------------- Won't Do



(1). Functional Requirements : What it does

   - user logs in, sign up
   - student watches the video
   - student likes the video
   - instructor creates the course, lessons
     upload video, upload pdf


(2). Non-Functional Requirements : How well it does it

    You need to ask
       
    This is not write ques: Do you want a highly avialable system - Yes 100% (No useful information)

    How to ask
       Ques - What wil happen if the system is down for 30 mins?
       Ans - 30 min disaster - other time students can tolerate. (insights)

       Availability

       uptime   99.9%   3 nines   ~8.76 hours / year
                99.99%  4 nines   ~52.9 mins / year
                99.999%  5 nines   ~5.26 mins / year

       Translate vague expectations into measurable/testable requirement


    
       Hexagon of NFR


       i. Availability
             What will happen if the system is down for 30 mins?
             
             Peak window, maintenance, uptime target
        
       ii. Scalability
             How many students do you expect over the next 6 months?

             Peak concurrent users, autoscaling, CDN

       iii. Consistency 
              When you update a lesson, is it okay if some student see the old version?

              cashing, acceptable staleness, cashe strategy

       iv. Security
              How worried are you about students sharing their login, download video?

              session limits, device limit, watermarking, DRM
       
       v. Performance
              Where are most of your students, and what devices and internet do they typically use?

              adaptive bitrate, mobile first, cache, cdn
        
       vi. Reliability
              If a student's module progress isn't saved, what would that affect for them?

              Which flow needs retries gurantees














"""