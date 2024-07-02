import numpy as np
import requests
import pandas as pd
from dateutil import parser
import re
from io import StringIO


def extract_dance_style(df_series):
    def extract_style(text):
        if 'salsa' in text:
            return 'salsa'
        elif 'bachata' in text:
            return 'bachata'
        else:
            return text
    return df_series.apply(extract_style)
def first_month_filter(xdf):
    return xdf[xdf['payment_method']=="one month pass - promo for new students only"]
def salsa_filter(xdf):
    return xdf[xdf['class_type'].str.contains('salsa')]

def bachata_filter(xdf):
    return xdf[xdf['class_type'].str.contains('bachata')]

def info_string(xdf):
    return f"""I've attended {len(xdf[xdf['status'] == "signed in"].index)} classes out of {len(xdf.index)} that I signed up for."""



filee = "/home/jay/PycharmProjects/kc_logistics/data/kc_logistics_corp_booking_data.csv"

html = """
<body class=" Enabled_DCA_MBNetworkDashboard Enabled_DCA_3rdPartyOpts Enabled_BUN_PurchLogo Enabled_BWE1_VideoTabUI Enabled_IPD_Reports_UI Enabled_SalonRefreshApptSchedule Enabled_5 Enabled_6 Enabled_7 Enabled_8 Enabled_1001 Enabled_1004 Enabled_1006 Enabled_1008 Enabled_1009 Enabled_1011 Enabled_1012 Enabled_1013 Enabled_1015 Enabled_1016 Enabled_1017 Enabled_1024 Enabled_1025 Enabled_1026 Enabled_1027 Enabled_1029 Enabled_1030 Enabled_1032 Enabled_1033 Enabled_1035 Enabled_1037 Enabled_1038 Enabled_1039 Enabled_1040 Enabled_1044 Enabled_1048 Enabled_1050 Enabled_1052 Enabled_1054 Enabled_1055"><div id="lightbox" style="opacity: 0.6; width: 1223px; height: 2960px; background: rgb(68, 68, 68); position: fixed; left: 0px; top: 0px; z-index: 10000; display: none;"></div>
    
<div id="pageWrapper">	
    
    <div id="fixedTop">
		<link rel="stylesheet" type="text/css" href="https://static.mindbodyonline.com/a/styles/simplelightbox_3790358322.css"><script type="text/javascript" src="https://static.mindbodyonline.com/a/scripts/plugins/jquery.simplelightbox_93863904.js"></script>
<style type="text/css">
	.logo-table{color: #0074d9; }
	.logo-table a:hover{text-decoration:underline;}
	.siteDeactivatedMsg
	{
		color:red;
		font-size: 20px;
		font-weight: bold;
	}
</style>
<div id="topSectionBG">
	
	<div id="topWrap" class="tablet-viewable">
	

	<table id="top-section-table" cellspacing="0" style="max-width: 960px; margin: 0 auto;">
		<tbody><tr>
			<td class="top-section-table-ends">
				<div id="top-logo-container">
					
    <a href="javascript:gotoStudioSite('http://stepsdancestudio.com');">
		<img id="studioLogoConsumer" style="max-width:300px; max-height:70px;" src="https://clients-content.mindbodyonline.com/studios/stepsdancestudioon/logo.gif?osv=637613603180000000" alt="">
	</a>

				</div>
			
			</td>
			<td>
			
				<div id="top-bb-container">
			<script type="text/javascript" src="https://static.mindbodyonline.com/a/scripts/bbincpartial_815644318.js"></script>
                    <script>
                        $(function() { ticker.init([""]); }); 
                    </script>
				<div id="memoryticker" style="max-width: 482px; max-height: 64px; display: block;"></div>
				
				</div>
			

			</td>
			<td id="top-login-container-td" class="top-section-table-ends">
				<div id="top-login-container">
					<script type="text/javascript" src="https://static.mindbodyonline.com/a/scripts/googletagmanager_4053830246.js"></script>

<script>
    // Required for global signout with Identity
    window.identityLogoutUrl  = '/asp/logout.asp?studioid=286172';
    window.manageFamilyUrl = '/IdentityLogin/FamilyAccountPicker/managefamilymembers';
    window.manageAccountUrl = 'https://account.mindbodyonline.com?subscriberId=286172';

    $(function() {
        // Add GTM script through JavaScript
        
    });

    displayLoginFailureOpts = {
        pageColor: "#0074d9",
        DisplayPhraseIncorrectEmailPassword: "The email or password you entered is incorrect.",
        DisplayPhraseSecurityverificationpending: "Security Verification Pending",
        DisplayPhraseInvalidlogin: "Invalid Login",
        DisplayPhraseLockoutnotice:"One more failed login attempt will lock this account out for 30 minutes.",
        DisplayPhraseRestrictedip: "Restricted IP",
        
            SeeStudioTopErrorStr: "Log in using your username or <a href=\"/PasswordRecovery/\">reset your password</a>.",
            SeeStudioBottomErrorStr: "<span style='color:#FF3333;margin-right:5px' id='LoginFailureSpan'>" +
                                        "It looks like you have a duplicate account or that a family member has the same email address as you. Please contact "+
                                        "Steps Dance Studio" +
                                        " at " + "!4166567837" +
                                        " to have your email or password changed.</span>"
        
    };
</script>

<div style="display:none;" id="loginpartialcss"><style type="text/css">.top-login-field-container             {                 padding-left: 5px;             }             .top-login-field-container a:hover             {                 text-decoration:underline;             }             #requiredtxtUserName, #requiredtxtPassword             {                 width: 100px;             }             #top-wel-sp             {                 -moz-border-radius: 5px 5px 5px 5px;                 border-radius: 5px 5px 5px 5px;                 padding: 0px 5px;             }             #last-login-sp             {                 -moz-border-radius: 5px 5px 5px 5px;                 border-radius: 5px 5px 5px 5px;                 padding: 0px 5px;                 font-size: 10px;                 float:right;             }             .logo-table{                 color: #0074d9;             }             #btnLogin             {                 text-transform:capitalize;             }<style></style></div>
<script type="text/javascript" src="https://static.mindbodyonline.com/a/scripts/loginpartial_2174347388.js"></script>
        <script type="text/javascript">
            function logOut() {
                parent.document.location.href = '/ASP/logout.asp?studioid=286172';
            }
        </script>
    

    <div class="logo-div">
        
            <table class="logo-table">
                <tbody><tr>
                    
                        <td><img src="https://static.mindbodyonline.com/a/asp/images/enso-20px.png"></td>
                    
                    <td style="white-space: nowrap;">
                        <span id="top-wel-sp">Welcome&nbsp;<span class="bold">Julien&nbsp;Ragbeer
<img src="https://static.mindbodyonline.com/a/asp/adm/images/mem-8.png" align="absmiddle" alt="">
</span>,&nbsp;you're signed in</span><br>

                        <span id="last-login-sp">Last sign-in:&nbsp;2024-06-28 2:41:15 PM</span>
                    </td>
                    <td>
                        <input id="btnLogout" type="button" class="logoutButton" value="Sign Out" onclick="logOutOfIdentity()">
                    </td>
                </tr>
            </tbody></table>
        
</div>

				</div>
				<div style="clear:both;"></div>
			</td>
		</tr>
	</tbody></table>
	</div>
	
<!---  2 -->


			<section class="top-nav-container">
				<div class="top-nav">
					<div class="tablet-hidden">
    <a href="javascript:gotoStudioSite('http://stepsdancestudio.com');">
		<img id="studioLogoConsumer" style="max-width:300px; max-height:48px;" src="https://clients-content.mindbodyonline.com/studios/stepsdancestudioon/logo.gif?osv=637613603180000000" alt="">
	</a>
</div>
					<div style="margin-left: auto;"></div>
					<!-- If Identity eventually uses this nav partial, add an asp file similar to LoginIdentityResponsivePartial. See TopnavDivPartial for reference-->
					<input id="nav-menu-toggle" type="checkbox">
					<label class="nav-menu-button-container" for="nav-menu-toggle">
						<div class="nav-menu-button"></div>
					</label>
					<ul class="nav-menu">
		
			<li class="tab tab-nosel tabclass" id="tabTD7" onclick="document.location.href='/classic/mainclass?fl=true&amp;tabID=7'">
				
						<div class="tab-l tab-l tab-l-firstTab"></div>
						<div class="tab-c tab-c tab-c-firstTab"><a id="tabA7">Schedule</a></div>
						<div class="tab-r tab-r tab-r-firstTab"></div>
						
			</li>
		
			<li class="tab tab-nosel tabenroll" id="tabTD8" onclick="document.location.href='/asp/main_enroll.asp?fl=true&amp;tabID=8'">
				
						<div class="tab-l tab-l tab-l-middleTab"></div>
						<div class="tab-c tab-c tab-c-middleTab"><a id="tabA8">Workshops</a></div>
						<div class="tab-r tab-r tab-r-middleTab"></div>
						
			</li>
		
			<li class="tab tab-nosel tabappts" id="tabTD9" onclick="document.location.href='/asp/main_appts.asp?fl=true&amp;tabID=9'">
				
						<div class="tab-l tab-l tab-l-middleTab"></div>
						<div class="tab-c tab-c tab-c-middleTab"><a id="tabA9">Privates</a></div>
						<div class="tab-r tab-r tab-r-middleTab"></div>
						
			</li>
		
			<li class="tab tab-nosel tabappts" id="tabTD102" onclick="document.location.href='/asp/main_appts.asp?fl=true&amp;tabID=102'">
				
						<div class="tab-l tab-l tab-l-middleTab"></div>
						<div class="tab-c tab-c tab-c-middleTab"><a id="tabA102">Assessments</a></div>
						<div class="tab-r tab-r tab-r-middleTab"></div>
						
			</li>
		
			<li class="tab tab-sel tabinfo" id="tabTD2" onclick="document.location.href='/asp/main_info.asp?fl=true&amp;tabID=2'">
				
						<div class="tab-l-sel tab-l-sel-middleTab"></div>
						<div class="tab-c-sel tab-c-sel-middleTab"><a id="tabA2">My info</a></div>
						<div class="tab-r-sel tab-r-sel-middleTab"></div>
						
			</li>
		
			<li class="tab tab-nosel tabshop" id="tabTD3" onclick="document.location.href='/asp/main_shop.asp?fl=true&amp;tabID=3'">
				
						<div class="tab-l tab-l-firstAfterSel tab-l-lastTab"></div>
						<div class="tab-c tab-c-firstAfterSel tab-c-lastTab"><a id="tabA3">Online store</a></div>
						<div class="tab-r tab-r-firstAfterSel tab-r-lastTab"></div>
						
			</li>
		
				<li class="sign-in-li">
					

<div style="display:none;" id="loginpartialcss"></div>

        <script type="text/javascript">
            function logOut() {
                parent.document.location.href = '/ASP/logout.asp?studioid=286172';
            }
        </script>

    <div class="logo-div">
        <table class="logo-table">
            <tbody><tr>
                <td style="white-space: nowrap;">
                    <span>Welcome&nbsp;<span class="bold">Julien&nbsp;Ragbeer
<img src="https://static.mindbodyonline.com/a/asp/adm/images/mem-8.png" align="absmiddle" alt="">
</span></span><br>

                    <span id="last-login-sp">Last sign-in:&nbsp;2024-06-28 2:41:15 PM</span>
                </td>
                <td style="padding-left: 20px">
                    <input id="btnLogoutResponsive" type="button" class="logoutButton" value="Sign Out" onclick="logOutOfIdentity()">
                </td>
            </tr>
        </tbody></table>
        
</div>

				</li>
				<li class="content-block">
    		</li>
			</ul></div></section>
		
</div>

	<div id="tabBottomBorder"></div>

	<div class="menu">
		
		<div class="menu-right">
			<a href="javascript:printWindow();" style="float: right; margin-top: 2px; margin-right: 17px;"><img src="https://static.mindbodyonline.com/a/asp/images/printer-20px.png" alt=""></a>
		</div>
		
	</div>


</div>
<div id="fixedTopShim"></div>

<script type="text/javascript" src="https://static.mindbodyonline.com/a/scripts/mb_3448370109.js"></script><link rel="stylesheet" type="text/css" href="https://static.mindbodyonline.com/a/styles/inc_sub_links_341918496.css"><link rel="stylesheet" type="text/css" href="https://static.mindbodyonline.com/a/styles/my_info_responsive_2719049593.css">
<style type="text/css">
#main {margin:0 auto;width:95%;}
caption {text-align:right;}
</style>


        <div class="wrapperTop">
            <div class="wrapperTopInner">
                <div class="pageTop">
                    <div class="pageTopLeft">
                        &nbsp; 
                    </div>
                    <div class="pageTopRight">
                        &nbsp; 
                    </div>
                </div>
            </div>
        </div>
          <div class="fixedHeader">
            <div class="sub-tab-bar group">
                <ul class="sub-tab-list">
                    <li class="first"><a class="sub-tab-link " href="/ASP/main_info.asp">Profile</a></li>
                    <li><a class="sub-tab-link " href="/ASP/my_sch.asp">My Schedule</a></li>
                    <li><a class="sub-tab-link  sub-tab-link-sel" href="/ASP/my_vh.asp">Visit History</a></li>
                     
                        <li><a class="sub-tab-link " href="/ASP/my_purch.asp">Purchase History</a></li>
                    
                    <li class=" last "><a class="sub-tab-link  " href="/ASP/my_ph.asp">Account</a></li>
                    
                </ul>
            </div>
        
          </div>
        
        <script type="text/javascript" src="https://static.mindbodyonline.com/a/scripts/coffee_664707950.js"></script><div id="wrapper-frame" style="position:relative;"><div id="wrapper-minheight"><div id="wrapper-bottompad"><div style="display:block;height:0;clear:both;">&nbsp;</div><div class="wrapper"><div id="main-content">
<h1>Visit History</h1>
	<div class="non-sub-tab-sub-tab-list-container">
		<a class="last" href="adm/adm_clt_canc.asp">Cancellation History</a>
	</div>
	<table class="myInfoTable" width="930" cellspacing="0">
		<thead>
			<tr class="tableHeader" style="">
				
					<th class="responsive-border-left">Day</th>
					<th class="responsive-no-border"></th>
				
				<th>Time</th>
				<th nowrap="" class="cell-tablet-viewable">Teacher</th>
				
				<th class="cell-tablet-viewable">Payment Method</th>
				<th>Class Type</th>
				<th class="cell-tablet-viewable">Status</th>
				<th class="cell-tablet-viewable">Web</th>
				<th class="cell-tablet-viewable">Payment Ref #</th>
				<th class="cell-tablet-viewable">&nbsp;</th>
			</tr>
		</thead>
		<tbody>

		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-28</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">Monthly Unlimited Auto Renew</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">294326</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-28</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">Monthly Unlimited Auto Renew</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">294326</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-28</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">Monthly Unlimited Auto Renew</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">294326</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-28</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>5:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Juan Pablo Painen</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">Monthly Unlimited Auto Renew</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">294326</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-26</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Wednesday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">Monthly Unlimited Auto Renew</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">294326</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-26</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Wednesday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">Monthly Unlimited Auto Renew</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">294326</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-26</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Wednesday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">Monthly Unlimited Auto Renew</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">294326</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-24</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Jason Ng</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-24</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Magaly Meza</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-24</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-23</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>4:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-23</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>3:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-23</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>2:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Body Movement Basics, All Levels</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-21</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#000000;">Absent</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-21</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>5:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Fernanda Martin</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#000000;">Absent</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-21</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#000000;">Absent</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-21</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#000000;">Absent</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-19</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Wednesday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-19</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Wednesday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-19</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Wednesday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-18</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">No</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-18</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Daniel Ospina Lopez</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-18</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Magaly Meza</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Traditional Bachata Partnerwork, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-18</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>9:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Daniel Ospina Lopez</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-17</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Kevin Sandoval</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">No</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-17</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Magaly Meza</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-17</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-17</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>9:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata Footwork, Levels 1-2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-16</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>2:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Body Movement Basics, All Levels</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-16</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>4:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-16</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>3:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-14</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-14</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-14</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-12</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Wednesday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Fernanda Martin</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left"> Body Movement for Salsa Dancers (Level 2-5)</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#000000;">Absent</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-12</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Wednesday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#000000;">Absent</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-11</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Magaly Meza</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Traditional Bachata Partnerwork, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-11</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>9:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-11</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-10</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Magaly Meza</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-10</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Jason Ng</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-10</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-10</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>9:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata Footwork, Levels 1-2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-09</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>4:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-09</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>3:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-09</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>2:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Kevin Sandoval</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-07</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Fernanda Martin</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-07</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-07</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-05</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Wednesday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">No</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-05</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Wednesday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-05</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Wednesday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-04</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>7:30&nbsp;PM</td>
			<td class="cell-tablet-viewable">Elia Garcia</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">Private Lesson, 1/2 Hour</span></td>
			
			<td align="left">Private Lesson, 1/2 Hour</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#000000;">No-Show</span>
			</td>
			<td class="cell-tablet-viewable">No</td>
			<td class="cell-tablet-viewable">293303</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-04</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-03</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-03</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Juan Pablo Painen</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-06-02</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>4:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-06-02</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>2:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Daniel Ospina Lopez</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-05-31</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-05-31</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Daniel Ospina Lopez</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-05-31</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Friday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Fernanda Martin</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-05-28</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>8:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-05-28</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-05-28</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-05-27</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>7:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Jason Ng</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#C00000;">Late Cancel</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-05-27</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Monday</td>
			<td>9:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Ernesto Campbell</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata Footwork, Levels 1-2</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#000000;">Absent</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-05-26</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>2:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Daniel Ospina Lopez</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-05-26</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Sunday</td>
			<td>1:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Kevin Sandoval</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">One Month Pass - Promo for NEW STUDENTS ONLY</span></td>
			
			<td align="left">Bachata, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Signed in</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282549</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#F2F2F2;">
			
				<td>2024-05-22</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Wednesday</td>
			<td>6:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Thamara Sutton</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">IN-PERSON Free Trial Class</span></td>
			
			<td align="left">Salsa, Level 1</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#000000;">Absent</span>
			</td>
			<td class="cell-tablet-viewable">No</td>
			<td class="cell-tablet-viewable">282547</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<img height="15px" width="1px" src="https://static.mindbodyonline.com/a/asp/images/trans.gif">
			
			</td>
		</tr>
              
			
		<tr style="background-color:#FAFAFA;">
			
				<td>2024-05-21</td>
				<td class="cell-tablet-hidden"></td>
			
			<td class="cell-tablet-viewable">Tuesday</td>
			<td>9:00&nbsp;PM</td>
			<td class="cell-tablet-viewable">Heather Kay</td>
			
			<td align="left" class="cell-tablet-viewable"><span class="truncate">From Salsa 1 to 2</span></td>
			
			<td align="left">Assessment for Salsa 2-3; Bachata 2-3</td>
			
			<td class="cell-tablet-viewable">
				<span style="color:#667D9A;">Completed</span>
			</td>
			<td class="cell-tablet-viewable">Yes</td>
			<td class="cell-tablet-viewable">282548</td>
			<td valign="middle" class="cell-tablet-viewable">
			
				<input type="button" onclick="document.location='adm/adm_appt_search_p.asp?qApptRefNo=21947&amp;tabID=102&amp;days=,1,2,3,4,5,6,7,';" value="Book Again">
			
			</td>
		</tr>
              
			
  </tbody></table>
</div></div></div></div></div>
</div><!-- pageWrapper -->

        <div id="footer" class="bt4">
	    <div id="ftLeft" class="frmLabel">
		    
		    <p>
			    <span> 2024-06-29 </span>
			    <span> 1:33:47 pm  </span>
			    <span> in </span>
			    <span> Ontario </span>
		    </p>
		    <p>
                <a href="https://www.mindbodyonline.com/privacy-policy" target="_mbswPrivacy" rel="nofollow noopener noreferrer">Privacy Policy</a>
                
			    <span>©2024 MINDBODY Inc.</span>
		    </p>
        </div>
        <div id="ftRight" style="height: 100%; margin: 0; display: flex; align-items: center;">
            <div id="subscriberFooterInfo" style="margin-bottom: 6px;">
                <div class="footerStudioIdContainer hidden">
                    <input class="footerStudioIdInput" aria-autocompletetype="text" name="name" readonly="" value="https://clients.mindbodyonline.com/classic/ws?studioid=286172">
                    <button class="secondaryBtn neutralBtn js-studioIdCopyButton" data-clipboard-target=".footerStudioIdInput"><i class="icon-copy"></i></button>
                </div>
                    <p><strong>Steps Dance Studio - 
                        <a href="#" class="js-studioIdLink">
                            Site ID: 286172
                        </a></strong>
                    
                            </p><p>819 Yonge Street 3rd floor, Toronto ON M4W 2G9</p>
                        
            </div>
            
                <a href="https://www.mindbodyonline.com/?ql=softwrfooter" target="_mbsw" rel="nofollow noopener noreferrer"><img src="https://static.mindbodyonline.com/a/images/logos/mb-new-logo-footer.png" alt="Powered by Mindbody Business" style="border:0px; height:25px; max-width: 200px;"></a> 	    
            
        </div>
    </div>
    
<script type="text/javascript">
$(function() {
	loginFocus();	
	makeContentScrollable(true, false, false);
    
	$(window).bind('GlobalMakeContentScrollable', function() {
		makeContentScrollable(true, false, false);
	});
	$(window).bind('resize', triggerMakeContentScrollable);
    
	if (document.location.hash) {
	document.location.hash = document.location.hash;
	}
});
</script>

<script defer="" src="https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015" integrity="sha512-ZpsOmlRQV6y907TI0dKBHq9Md29nnaEIPlkf84rnaERnq6zvWvPUqr2ft8M1aS28oN72PdrCzSjY4U6VaAw1EQ==" data-cf-beacon="{&quot;rayId&quot;:&quot;89b7a9deaa7cab4e&quot;,&quot;version&quot;:&quot;2024.4.1&quot;,&quot;token&quot;:&quot;92e90509f0f4454ca3ded5f7238c589c&quot;}" crossorigin="anonymous"></script>


<div id="tooltip" style="display: none; left: 23px; right: auto; top: 15px;"><h3>Click here to return to the Steps Dance Studio homepage.</h3><div class="body" style="display: none;"></div><div class="url" style="display: none;"></div></div><div class="mbpopoverContainer mbpopoverContainer--loading">                                 <div class="mbpopoverContainer-top mbpopoverContainer-top--under"></div>                                 <div class="mbpopoverContainer-top mbpopoverContainer-top--over"></div>                                 <div class="mbpopoverContainer--loadingContainer">                                     <div></div>                                     <div></div>                                     <div></div>                                 </div>                                 <div class="mbpopoverContainer-bottom mbpopoverContainer-bottom--under"></div>                                 <div class="mbpopoverContainer-bottom mbpopoverContainer-bottom--over"></div>                             </div></body>
"""

idf = pd.read_html(StringIO(str(html)))[3]
idf = idf.dropna(axis=1, how='all')
# fix the column names
idf.columns = [i.lower().replace(" ", "_") for i in idf.columns]
new_cols = [f'time{x}' for x in range(2)]
idf.columns = ['date'] + new_cols + list(idf.columns)[2:-1]
# create a timestamp column
idf = idf.drop(columns=['time0'])
idf['timestamp'] = pd.to_datetime([a + ' ' + b for a,b in zip(idf['date'], idf['time1'])])
cl = []
ct = []
for i in idf['class_type']:
    try:
        new = i.split(',')
        cl.append(new[1])
        ct.append(new[0])
    except:
        cl.append(i)
        ct.append(i)
idf['class_level'] = cl
idf['class_type'] = ct

for x in ['class_type', "class_level", "status", "payment_method"]:
    idf[x] = idf[x].str.lower()

# remove columns that aren't so useful and sort the df
idf = idf.sort_values("timestamp", ascending=True)
idf = idf[["timestamp","teacher","class_type","class_level", "payment_method","status",
           #"web","payment_ref_#","date","time1",
           ]]
idf['class_name'] = idf['class_type']
# remove assessments and private lessons
idf = idf[~idf['class_name'].isin(['private lesson'])]
idf = idf[~idf['class_name'].str.contains('assessment')]
# fix the class_level column
temp_df = idf[idf['class_level'].str.contains('all')]
idf.loc[temp_df.index,'class_level'] = "1-2-3-4-5"
idf['class_level'] = idf['class_level'].str.extract(r'(\d)')
idf['class_type'] = extract_dance_style(idf['class_type'])



first_month_df = first_month_filter(idf)
first_month_salsa_df = salsa_filter(first_month_filter(idf))
pp = info_string(first_month_df)
print("First Month: " + pp)
pp = info_string(first_month_salsa_df)
print("First Month + Salsa: " + pp)
print(first_month_df['class_type'].value_counts())
print(idf['class_type'].value_counts())



