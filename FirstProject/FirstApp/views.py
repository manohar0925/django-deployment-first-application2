from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function

	#ss ----> is html-data/code
	ss = '''		
			<center>
				<h2 style="color:Blue;">
					Hello User, Welcome to Django First-Project First-App
				</h2>
				<hr />
			</center>
		''';
	
	return HttpResponse(ss);
    
def show(request):
    ss='''
        <!--
	HTML Webpage to display "Welcome-Message" with different Headings 
	(E:\MANU\HTML\Welcome.html)
	-->
<html>
	<head>
		<title>*** WELCOME TO THIS PAGE***</title>
		<STYLE>
			H1{
				COLOR:BLUE;
			}
			H2{
				COLOR:GREEN;
			}
			H3{
				COLOR:PINK;
			}
			H4{
				COLOR:BROWN;
			}
			H5{
				COLOR:VIOLET;
			}
			H6{
				COLOR:RED;
			}
			H1,H3,H5{
				BACKGROUND-COLOR:YELLOW;
			}
			H2,H4,H6{
				BACKGROUND-COLOR:LIGHTGREEN;
			}
		</STYLE>
	</head>
	<body>
		<CENTER>
			<H1> WELCOME TO MY WEB PAGE</H1>
			<HR COLOR='BLUE' WIDTH='95%'/>
			<H2> THIS IS MANOHAR</H2>
			<HR COLOR='BLUE' WIDTH='85%'/>
			<H3> HI MANOHAR </H3>
			<HR COLOR='BLUE' WIDTH='75%'/>
			<H4> WELCOME TO MANU</H4>
			<HR COLOR='BLUE' WIDTH='65%'/>
			<H5> DO U HAVE GIRL FRND </H5>
			<HR COLOR='BLUE' WIDTH='55%'/>
			<H6> NO BUT I HAVE BESTIE </H6>
			<HR COLOR='BLUE' WIDTH='45%'/>
		</CENTER>
	</body>
</html> 
    
    '''
    return HttpResponse(ss);


def hello(request):
	print("hello/ url is requested & hello() is executed");
	ss='''
	<html>
		<head>
			<title>Hello Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightblue;
					border:2px dotted Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Hello User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Welcome to Django-App</h2>
				<hr color='brown' width='60%'/>
				<h3>Have a nice day...</h3>
				<hr color='brown' width='40%'/>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);
    
import time;	
def senddatetime(request):
	print("dtime/ url is requested & senddatetime() is executed");
	ct = time.ctime()
	print("Client Request Date & time on server :: ",ct);
	ss='''
	<html>
		<head>
			<title>Date-time Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightgreen;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Welcome to DJango-User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Server-Date & Time :: </h2>
				<hr color='brown' width='70%'/>
				<h3>''',ct,'''</h3>
				<hr color='brown' width='60%'/>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);

def demo(request):
    print('demo is excuted')
    s='''
        <center>
            <h1> HI MANOHAR WELCOME    </h1>
            <hr/>
            <h2> GOOD MORNING </h2>
        </center>
       
    '''
    return HttpResponse(s);

def homepage(request):
    print('home page is excuted')
    manu='''
        <center>
            <h1> welcome to home page <h1>
            <hr/>
            <h2>😁 page not found 😁 </h2>
        </center>
    '''
    return HttpResponse(manu);