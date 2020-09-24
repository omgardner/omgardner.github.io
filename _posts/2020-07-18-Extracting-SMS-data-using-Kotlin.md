---
layout: post
title: Extracting SMS data using Kotlin
categories: [mobile, programming]
tags: [android, mobile, programming, kotlin, android-studio, java, security]

permalink: /kotlin-sms-extractor-app/
excerpt_separator: <!--more-->
---
![sb-12](/images/kotlin-sms-extractor-app/composite-1.png)

>  The UI design / storyboard for my Kotlin app.

I have created an app in Kotlin that extracts my SMS messages and sends them to my computer. This is part of a bigger project where I retrieve and analyse all the messages I have ever received across multiple mediums such as SMS, WhatsApp and Facebook Messenger.

<!--more-->

## Quick rundown of what I learned from this project

- How to use Android Studio
- How to program in Kotlin
- How to properly use IDEs to augment my workflow.
- Android data structure
    - ContentProviders
    - queries
    - Requesting and listening for permissions.
    - Interactions between UI and code.
    
## Code
I have setup a [GitHub repo](https://github.com/omgardner/RetrieveSMSMessages) to hold the code. To jump straight to the activity file containing all the code, click [here](https://github.com/omgardner/RetrieveSMSMessages/blob/master/app/src/main/java/com/omgardner/retrievesmsmessages/MainActivity.kt).
    

## Why am I programming my own app?

There are numerous [existing apps](https://play.google.com/store/search?q=SMS%20Backup&c=apps) on the play store of which I could have used. However due to the sensitive nature of the data I didn't feel confident giving a random 3rd party access to my data. 

Also I have been interested in mobile app-dev for a while now, and this was a great excuse to finally learn how to make an app.

## How the app works

![diagram](../images/kotlin-sms-extractor-app/diagram.png)

> Fig 1. An overview of the app's logical flow. Arrows indicate sequential order. Each UI button press corresponds to the 3 steps above from top-to-bottom.

### Step 1: Requests the READ_SMS Permission

![sb-12](/images/kotlin-sms-extractor-app/composite-1.png)

> The change in UI state: (a) started app, (b) permissions successfully granted, (c) data successfully retrieved.

All I needed was the READ_SMS permission to access the SMS Inbox and Outbox data. Other data, such as images and group SMS conversations would likely require READ_MMS permissions.

- A list of all the permissions can be found [here](https://developer.android.com/reference/kotlin/android/Manifest.permission)

Certain UI elements are locked by me until the app is granted appropriate permissions. To check for an update to the permission I used Kotlin's Observable Delegates. 

```kotlin
var allPermissionsGranted : Boolean by Delegates.observable(false) { 
    _, _, newValue ->
    	btnReadSmsInbox.isClickable = newValue
    // more UI code below
}
```

> Example code that enables or disables a button based on the boolean state of the variable. 

`allPermissionsGranted` is a boolean observable delegate that runs a piece of code each time the variable's state is changed. In my case the code updates the UI, enabling the button that begins Step 2.

### Step 2: Extracts the SMS data into a JSON file

Here's a run-down of how the data is stored inside an Android device:

The data is stored in one of many internal database files called ***Data Storage***. In order to enforce security you cannot access the ***Data Storage*** directly. Instead, you [query](https://developer.android.com/reference/kotlin/android/content/ContentProvider?hl=en#query) a ***ContentProvider*** that will check if the app is authorized to access the data. If the query is authorized and the query returns some results the query function returns a *cursor* object.

The cursor object is then iterated over to generate a JSON array of objects containing key:value pairs in the form of column:value_in_row.

#### A mistake I made here:

> SMS Inbox only contains the **RECEIVED** messages. It took me an hour of debugging to realise that my missing **SENT** messages were located in the SMS Outbox instead.

#### Why JSON?

I chose JSON as the data is [semi-structured](https://en.wikipedia.org/wiki/Semi-structured_data): meaning that I could easily change the number of SMS columns used without affecting future analyses. There are alternatives to this, but this method makes it very easy to be read by Python in the later analyses of the data.

### Step 3: Exports the JSON file as an attachment via an Intent

What is an **Intent**? An **Intent** is a way to let other apps on the phone do things with your data. An example is the share button in a photo app. There will be a screen showing the various apps that contain the necessary code to process such an **Intent**.

This is easily done by using a template called [the Android ShareSheet](https://developer.android.com/training/sharing/send#using-android-system-sharesheet). Just like the photo app can send an image, you can send any file; a.k.a. [binary content](https://developer.android.com/training/sharing/send#send-binary-content). To send my JSON file - or any file for that matter - all that is needed is:

- A URI location of the file. This can be generated from a filepath using the `FileProvider.getUriForFile` function.
- the MIME type. This can be hardcoded or can be found using the `contentResolver.getType(fileUri)` function.

From here, by selecting the Gmail app you can send the file as an attachment to yourself. Make sure not to accidentally send the file to someone else (I triple checked each time I did this)!

![sb-3](/images/kotlin-sms-extractor-app/composite-2.png)

> Step 3 as seen via the app.

#### A mistake I made here:

> I should have explored quicker options for debugging the app than emailing it to myself. The debugging process was this: 
>
> - Find a logic error --> start the APP --> re-fetch the SMS data --> create intent --> select my email --> make sure that I don't send my SMS data to a random person --> download the JSON file attachment via my PC --> test the data --> repeat if still broken.
>
> Note: I also used Android's [logging](https://developer.android.com/reference/android/util/Log.html) capabilities to reduce the amount of times I did the above steps to a minimum.
>
> It wasn't worth the time investment to change the process since I was nearly done when I realised this mistake ([relevant xkcd](https://xkcd.com/1205/)). An alternative would be to send the file to a local server, and programmatically retrieve the data upon update.

## Resources that I considered

### Articles

The [official Android developer documentation](https://developer.android.com/guide/components/fundamentals) was surprisingly comprehensive, and contained code examples for both Kotlin and Java. 

### Video Resources

- [How to Kotlin - from the Lead Kotlin Language Designer (Google I/O '18)](https://www.youtube.com/watch?v=6P20npkvcb8)
    - This was great for understanding Kotlin, especially how it functionally compares to languages like Java and Python.

- [Android Kotlin Beginner Tutorial (Google I/O '17)](https://www.youtube.com/watch?v=sZWMPYIkNd8)
    - This was vital for my understanding of how the Kotlin code interacts with the UI, as well as the design philosophy behind an Android Studio Project.
    - Taught me the  minimum requirements for an app. Helpful for understanding the source code of other apps.

### Existing open-source apps 

[gtalksms](https://code.google.com/archive/p/gtalksms/source/default/source), a open-source SMS app. **I chose to ignore it** at the time for a few reasons:

- I didn't know the first thing about android app development, and I found it confusing to understand what components were absolutely necessary.
    - I learn a LOT better from the bottom-up rather than from the top-down.
- I wanted to program in Kotlin, not just Java.

I chose Kotlin due to my university experience with Java. It was a decent challenge as for the past 2 years I have been programming mostly in Python. 

## What next?

### It's part of a bigger project

I'm using the data as part of a bigger analysis on my messaging habits across platforms. Currently I have collected and parsed my WhatsApp, Facebook Messenger and SMS messages. The data then goes into a sqlite3 DB. 

### Future data exploration

In a future article I will work on some interesting visualisations to visually understand the flow and frequency of conversations (that I have). This will help me answer random questions like:

- How long does it take for me to respond to a message on a Thursday?
- Using semantic analysis, do my messages reflect my mood? 
    - Do I have happier conversations with closer friends?
    - Can I work out the category of the person: are they a friend? family member? work colleague based on this?
- Do I swear a lot when talking to different people? 
- What time of day do I respond to messages the most? The least?
- How have my messaging habits changed over time?
- Do I communicate differently with the same person when a different platform (WhatsApp vs SMS, for example) is used?

### Thanks for reading! 

If you have any feedback you would like to share, I can be reached on twitter @o_m_gardner, or reddit u/omgardner
