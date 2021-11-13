# Отчёт по пентесту тестового приложения.
## Scope 

        image: innost5/netology_postgres:latest

        image: innost5/netology_app:latest
        
## Information from OSINT

## Vulnerabilities

# 1
### Name
p-XSS
Cross Site Scripting (Persistent) 
### Severity
High
### Steps to reproduse

    </li><script>alert(1);</script><li>

### How to fix 

Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.
Examples of libraries and frameworks that make it easier to generate properly encoded output include Microsoft's Anti-XSS library, the OWASP ESAPI Encoding module, and Apache Wicket.

In general, effectively preventing XSS vulnerabilities is likely to involve a combination of the following measures:

- Filter input on arrival. At the point where user input is received, filter as strictly as possible based on what is expected or valid input.
-    Encode data on output. At the point where user-controllable data is output in HTTP responses, encode the output to prevent it from being interpreted as active content. Depending on the output context, this might require applying combinations of HTML, URL, JavaScript, and CSS encoding.
- Use appropriate response headers. To prevent XSS in HTTP responses that aren't intended to contain any HTML or JavaScript, you can use the Content-Type and X-Content-Type-Options headers to ensure that browsers interpret the responses in the way you intend.
- Content Security Policy. As a last line of defense, you can use Content Security Policy (CSP) to reduce the severity of any XSS vulnerabilities that still occur.

# 2
### Name
XSS
Cross Site Scripting (Reflected) 
### Severity
High
### Steps to reproduse

    </li><script>alert(1);</script><li>

### How to fix 

Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.
Examples of libraries and frameworks that make it easier to generate properly encoded output include Microsoft's Anti-XSS library, the OWASP ESAPI Encoding module, and Apache Wicket.

In general, effectively preventing XSS vulnerabilities is likely to involve a combination of the following measures:

- Filter input on arrival. At the point where user input is received, filter as strictly as possible based on what is expected or valid input.
-    Encode data on output. At the point where user-controllable data is output in HTTP responses, encode the output to prevent it from being interpreted as active content. Depending on the output context, this might require applying combinations of HTML, URL, JavaScript, and CSS encoding.
- Use appropriate response headers. To prevent XSS in HTTP responses that aren't intended to contain any HTML or JavaScript, you can use the Content-Type and X-Content-Type-Options headers to ensure that browsers interpret the responses in the way you intend.
- Content Security Policy. As a last line of defense, you can use Content Security Policy (CSP) to reduce the severity of any XSS vulnerabilities that still occur.

# 3

### Name
Vulnerable JS Library
### Severity
Medium
### Steps to reproduse

jquery-3.2.1.min.js

### How to fix 

Please upgrade to the latest version of jquery.

# 4

### Name
X-Frame-Options Header Not Set
### Severity
Medium
### Steps to reproduse

X-Frame-Options header is not included in the HTTP response to protect against 'ClickJacking' attacks.

### How to fix 
Most modern Web browsers support the X-Frame-Options HTTP header. Ensure it's set on all web pages returned by your site (if you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's "frame-ancestors" directive.

# 5
### Name
Absence of Anti-CSRF Tokens
### Severity
Low
### Steps to reproduse

<form class="col s12" method="POST">

### How to fix 
Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.
For example, use anti-CSRF packages such as the OWASP CSRFGuard.

# 6
### Name
Application Error Disclosure
### Severity
low
### Steps to reproduse

HTTP/1.1 500 Internal Server Error

### How to fix 
Review the source code of this page. Implement custom error pages. Consider implementing a mechanism to provide a unique error reference/identifier to the client (browser) while logging the details on the server side and not exposing them to the user.

# 7
### Name
Application Error Disclosure
### Severity
low
### Steps to reproduse

HTTP/1.1 500 Internal Server Error

### How to fix 
Review the source code of this page. Implement custom error pages. Consider implementing a mechanism to provide a unique error reference/identifier to the client (browser) while logging the details on the server side and not exposing them to the user.

# 8
### Name
Cookie No HttpOnly Flag
### Severity
low
### Steps to reproduse

Set-Cookie: AIOHTTP_SESSION

### How to fix 
Ensure that the HttpOnly flag is set for all cookies.