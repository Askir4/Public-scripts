# Mail Faker GUI

**Warning: For internal test purposes only!**

---

## Table of Contents

1. [Description](#description)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
4. [Running the Script](#running-the-script)  
5. [GUI Elements & Functions](#gui-elements--functions)  
6. [Dark Mode & Authentication](#dark-mode--authentication)  
7. [Add Attachment](#add-attachment)  
8. [Error Handling](#error-handling)  
9. [Disclaimer](#disclaimer)

---

## Description

This PowerShell script provides a simple graphical user interface (GUI) to send test emails with **any sender and recipient addresses** via an SMTP server.  
**IMPORTANT:** This tool is intended exclusively for internal testing and must not be used in production environments!

---

## Prerequisites

- Windows PowerShell (version 5.1 or higher)  
- .NET Framework with `System.Windows.Forms` and `System.Drawing`  
- Network access to an SMTP server (port 25, 465, 587 or 2525)  

---

## Installation

1. Copy the script file **`Mail-faker-gui-03.ps1`** to a local folder.  
2. Start PowerShell with **Administrator rights** (if required).  
3. Adjust Execution Policy if needed:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
