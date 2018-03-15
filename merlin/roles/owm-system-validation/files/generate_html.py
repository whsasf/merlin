import os
# Generates HTML

def process_line(res,key):
	msg_key=""
	for line in res[key]:
		msg_key+="""<tr><td><p>"""
		msg_key+=line
		msg_key+= """</p></td></tr>"""
        return msg_key

message_header = """ <html>
			<head>	
				<link href='http://fonts.googleapis.com/css?family=Merriweather&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
				<style>
					 *{
						font-family: 'Merriweather', Arial, sans-serif;
					 }
					 body, html {
						  height: 100%;
						  margin: 0;
						  -webkit-font-smoothing: antialiased;
						  font-weight: 100;
						  text-align: center;
						  background-color: #fafafa;
					  }
					  .tabs input[type=radio] {
						  position: absolute;
						  top: -9999px;
						  left: -9999px;
					  }
					  .tabs {
						width: 100%;
						float: none;
						list-style: none;
						position: relative;
						padding: 0;
					  }
					  .tabs li{
						float: left;
					  }
					  .tabs label {
						  font-size: 13px;
						  text-transform: uppercase;
						  padding: 10px 20px;
						  letter-spacing: .2rem;
						   line-height: 2.3rem;
						  color: #222;
						  font-weight: 400;
						  font-family: 'Lily Script One', helveti;
						  cursor: pointer;
						  position: relative;
						  top: 30px;
						  bottom: 3px;
						  -webkit-transition: all 0.2s ease-in-out;
						  -moz-transition: all 0.2s ease-in-out;
						  -o-transition: all 0.2s ease-in-out;
						  transition: all 0.2s ease-in-out;
					  }
					  .tabs label:hover {
						color: #1EAEDB;
						top: 30px;
					  }
					  [id^=tab]:checked + label {
						color: #1EAEDB;
						top: 30px;
					  }
					  [id^=tab]:checked ~ [id^=tab-content] {
						  display: block;
					  }
					  .tab-content{
						z-index: 2;
						display: none;
						text-align: left;
						width: 100%;
						font-size: 20px;
						line-height: 140%;
						padding-top: 10px;
						/* background: #08C; */
						padding: 15px;
						/* color: white; */
						position: absolute;
						top: 100px;
						left: 0;
						box-sizing: border-box;
						-webkit-animation-duration: 0.5s;
						-o-animation-duration: 0.5s;
						-moz-animation-duration: 0.5s;
						animation-duration: 0.5s;
					  }
					  .title {
						  color: rgb(34, 34, 34);
						  display: block;
						  font-size: 25px;
						  font-weight: 300;
						  height: 32px;
						  letter-spacing: .1rem;
						  line-height: 52.5px;
						  margin-bottom: 20px;
						  margin-top: 0px;
						  text-align: center;
						}
					  .divClass{
							width: 41%; 
							float:left; 
							height:400px;
							background:rgb(246,248,255);
							 margin: 10px;
							 margin-left: 90px;
							 overflow: scroll;
							border: 2px solid #a1a1a1;
							box-shadow: 5px 5px 5px #888888;
							}
						.log_div_Class2{
							width: 90%;
							float:left; 
							height:600px;
							background:rgb(246,248,255);
							 margin: 10px;
							 margin-left: 90px;
							 overflow: scroll;
							 border: 2px solid #a1a1a1;
							 box-shadow: 5px 5px 5px #888888;
							}		
					.blank_div{
							width: 100%;
							height:50px;
							}
					.wrap_class{
							width: 90%;
							float:left; 
							height:50px;
							 margin-left: 90px;
							 text-align: center;
							}
					h3 {
							text-align: center;
							color: #1EAEDB;
							font-weight: 400;
							 font-size: 19px;
						}
					h1 {
							text-align: center;
							border-bottom: 4px solid #A9A9A9;
						}
					h2{
						 color: rgb(34, 34, 34);
						  display: block;
						  font-size: 30px;
						  font-weight: 300;
						  height: 32px;
						  letter-spacing: .1rem;
						  line-height: 52.5px;
						  margin-bottom: 20px;
						  margin-top: 0px;
						  text-align: center;
						}
					h5{
						  max-width: 100%;
						  letter-spacing: .05rem;
						  display:block; 
						  float:left; 
						  margin:0;
						  padding:5px;
						  font-size: 12px;
						  text-transform: uppercase;
						  font-weight: 600;
						  color: #009587;
						  text-align: left;
						}
					table
						{
						  margin: 0;
						  border-collapse: collapse;
						  text-align: left;
						  table-layout:fixed;
						}
					table th, 
					table td {
					  padding: 5px;
					  max-width: 250px;
					  word-wrap: break-word;
					} 
					table th
					{
					  font-weight: 600;
					  text-transform: uppercase;
					  border-bottom: 1px solid #f1f1f1;
					}
					table td
					{
					  border-bottom: 1px solid #f1f1f1;
					  padding: 9px 8px;
					}
					table tbody tr:hover td
					{
					  background-color: #fafafa;
					}
					table.metrics-table {
					  text-align: center;
					}
					.heading
					{
							width: 90%;
							float:left; 
							height:50px;
							 margin-top: 0px;
							 margin-bottom: 30px;
					}
					.more {
					  display: none;
					  }
				   a.showLink, a.hideLink {
					  text-decoration: none;
					  /*color: #009587;*/
					  font-weight: 400;
					  font-size: 19px;
					   width: 90%;
					  float:left; 
					  }
				   a.hideLink {
					  background: transparent url(up.gif) no-repeat left; }
				   a.showLink:hover, a.hideLink:hover {
					  color: #1EAEDB;
					  }
				</style>
			</head>"""

def gen_main_html(res_1,res_2,res_3,res_4,res_5,res_6,res_7,res_8,res_9,res_10,res_11,res_12,res_13,res_14,res_15,res_16,res_17):
	message = message_header
	message += """ 
				<body>
				<br><br>
					<h2 class="title">Messaging Server's Administration Data :<br><br></h2>
					<ul class="tabs">
					<li>
					  <input type="radio" checked name="tabs" id="tab1">
					  <label for="tab1">mta</label>
					  <div id="tab-content" class="tab-content animated fadeIn">
					"""
	res_1_keys = res_1.keys()
	if res_1_keys:
		for key in res_1_keys:
			print "key",key
			html_link_mta = '"'+res_1[key]+'"'
			message+="""<div id="res_1" class="wrap_class">
								<p><a href="""+html_link_mta+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
	else :
		message+="""<div id="res_1_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For MTA </font></p></td></tr></table>
						</div>
						"""
	message+=""" </div>
					</li>
					<li>
					  <input type="radio" name="tabs" id="tab2">
					  <label for="tab2">imap</label>
					  <div id="tab-content2" class="tab-content animated fadeIn">
					  """
	
	res_2_keys = res_2.keys()
	if res_2_keys:
		for key in res_2_keys:
			print "key",key
			html_link_imap = '"'+res_2[key]+'"'
			message+="""<div id="res_2" class="wrap_class">
								<p><a href="""+html_link_imap+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
	else :
		message+="""<div id="res_2_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For IMAP </font></p></td></tr></table>
						</div>
						"""
	message+=""" 	</div>
					</li>
					<li>
					  <input type="radio" name="tabs" id="tab3">
					  <label for="tab3">pop</label>
					  <div id="tab-content3" class="tab-content animated fadeIn">
					  """	
	res_3_keys = res_3.keys()
	if res_3_keys:
		for key in res_3_keys:
			html_link = '"'+res_3[key]+'"'
			message+="""<div id="res_3" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""

	else :
		message+="""<div id="res_3_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For POP </font></p></td></tr></table>
						</div>
						"""
					  
	message+=""" 	</div>
					</li>
					
					<li>
					  <input type="radio" name="tabs" id="tab4">
					  <label for="tab4">mss</label>
					  <div id="tab-content4" class="tab-content animated fadeIn">
					  """
					  
	res_4_keys = res_4.keys()
	if res_4_keys:
		for key in res_4_keys:
			html_link = '"'+res_4[key]+'"'
			message+="""<div id="res_4" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
			
	else :
		message+="""<div id="res_4_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For MSS </font></p></td></tr></table>
						</div>
						"""
					  
	message+=""" 	</div>
					</li>
					<li>
					  <input type="radio" name="tabs" id="tab5">
					  <label for="tab5">mxos</label>
					  <div id="tab-content5" class="tab-content animated fadeIn">
					  """
	res_5_keys = res_5.keys()
	if res_5_keys:
		for key in res_5_keys:
			html_link = '"'+res_5[key]+'"'
			message+="""<div id="res_5" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
	else :
		message+="""<div id="res_5_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For MXOS </font></p></td></tr></table>
						</div>
						"""
					  
	message+=""" 	</div>
					</li>
					
					<li>
					  <input type="radio" name="tabs" id="tab6">
					  <label for="tab6">App Suite</label>
					  <div id="tab-content6" class="tab-content animated fadeIn">
					  """
	res_6_keys = res_6.keys()
	if res_6_keys:
		for key in res_6_keys:
			html_link = '"'+res_6[key]+'"'
			message+="""<div id="res_6" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""

	else :
		message+="""<div id="res_6_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For App Suite </font></p></td></tr></table>
						</div>
						"""
					  
	message+=""" 	</div>
					</li>
					<li>
					  <input type="radio" name="tabs" id="tab7">
					  <label for="tab7">Cassandra meta</label>
					  <div id="tab-content7" class="tab-content animated fadeIn">
					  """
	res_7_keys = res_7.keys()
	if res_7_keys:
		for key in res_7_keys:
			html_link = '"'+res_7[key]+'"'
			message+="""<div id="res_7" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""

	else :
		message+="""<div id="res_7_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For Cassandra Meta </font></p></td></tr></table>
						</div>
						"""
					  
	message+=""" 	</div>
					</li>
					<li>
					  <input type="radio" name="tabs" id="tab8">
					  <label for="tab8">Cassandra blob</label>
					  <div id="tab-content8" class="tab-content animated fadeIn">
					  """
	res_8_keys = res_8.keys()
	if res_8_keys:
		for key in res_8_keys:
			html_link = '"'+res_8[key]+'"'
			message+="""<div id="res_8" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
			
	else :
		message+="""<div id="res_8_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For Cassandra Blob </font></p></td></tr></table>
						</div>
						"""
					  
	message+=""" 	</div>
					</li>
					
					<li>
					  <input type="radio" name="tabs" id="tab9">
					  <label for="tab9">mysqlDB</label>
					  <div id="tab-content9" class="tab-content animated fadeIn">
					  """
	res_9_keys = res_9.keys()
	if res_9_keys:
		for key in res_9_keys:
			html_link = '"'+res_9[key]+'"'
			message+="""<div id="res_9" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
	else :
		message+="""<div id="res_9_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For MYSQLDB </font></p></td></tr></table>
						</div>
						"""
					  
	message+=""" 	</div>
					</li>
					
					<li>
					  <input type="radio" name="tabs" id="tab10">
					  <label for="tab10">nginx</label>
					  <div id="tab-content10" class="tab-content animated fadeIn">
					  """
	res_10_keys = res_10.keys()
	if res_10_keys:
		for key in res_10_keys:
			html_link = '"'+res_10[key]+'"'
			message+="""<div id="res_10" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
	else :
		message+="""<div id="res_10_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For NGINX </font></p></td></tr></table>
						</div>
						"""

	message+=""" 	</div>
					</li>
					<li>
					  <input type="radio" name="tabs" id="tab11">
					  <label for="tab11">imqueueserv</label>
					  <div id="tab-content11" class="tab-content animated fadeIn">
					  """					  
	res_11_keys = res_11.keys()
	if res_11_keys:
		for key in res_11_keys:
			html_link = '"'+res_11[key]+'"'
			message+="""<div id="res_11" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
	else :
		message+="""<div id="res_11_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For imqueueserv </font></p></td></tr></table>
						</div>
						"""
	
	message+=""" 	</div>
					</li>
					<li>
					  <input type="radio" name="tabs" id="tab12">
					  <label for="tab12">imextserv</label>
					  <div id="tab-content12" class="tab-content animated fadeIn">
					  """	
	res_12_keys = res_12.keys()
	if res_12_keys:
		for key in res_12_keys:
			html_link = '"'+res_12[key]+'"'
			message+="""<div id="res_12" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
	else :
		message+="""<div id="res_12_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For imextserv </font></p></td></tr></table>
						</div>
						"""
					  
	message+=""" 	</div>
					</li>
					<li>
					  <input type="radio" name="tabs" id="tab13">
					  <label for="tab13">imdirserv</label>
					  <div id="tab-content13" class="tab-content animated fadeIn">
					  """	
	
	res_13_keys = res_13.keys()
	if res_13_keys:
		for key in res_13_keys:
			html_link = '"'+res_13[key]+'"'
			message+="""<div id="res_13" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
	else :
		message+="""<div id="res_13_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For imdirserv </font></p></td></tr></table>
						</div>
						"""
					  
	message+=""" 	</div>
					</li>
					<li>
					  <input type="radio" name="tabs" id="tab14">
					  <label for="tab14">immgrserv</label>
					  <div id="tab-content14" class="tab-content animated fadeIn">
					  """	
					  
	res_14_keys = res_14.keys()
	if res_14_keys:
		for key in res_14_keys:
			html_link = '"'+res_14[key]+'"'
			message+="""<div id="res_14" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
			
	else :
		message+="""<div id="res_14_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For immgrserv </font></p></td></tr></table>
						</div>
						"""
		
	message+=""" 	</div>
					</li>
					<li>
					  <input type="radio" name="tabs" id="tab15">
					  <label for="tab15">imconfserv</label>
					  <div id="tab-content15" class="tab-content animated fadeIn">
					  """	
					  
	res_15_keys = res_15.keys()
	if res_15_keys:
		for key in res_15_keys:
			html_link = '"'+res_15[key]+'"'
			message+="""<div id="res_15" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
	else :
		message+="""<div id="res_15_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For imconfserv </font></p></td></tr></table>
						</div>
						"""
					  
	message+=""" 	</div>
					</li>
					<li>
					  <input type="radio" name="tabs" id="tab16">
					  <label for="tab16">imdircacheserv</label>
					  <div id="tab-content16" class="tab-content animated fadeIn">
					  """	
					  
	res_16_keys = res_16.keys()
	if res_16_keys:
		for key in res_16_keys:
			html_link = '"'+res_16[key]+'"'
			message+="""<div id="res_16" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
			
	else :
		message+="""<div id="res_16_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For imdircacheserv </font></p></td></tr></table>
						</div>
						"""
		
					  
	message+=""" 	</div>
					</li>
					<li>
					  <input type="radio" name="tabs" id="tab17">
					  <label for="tab17">IMDIRSERVSEC</label>
					  <div id="tab-content17" class="tab-content animated fadeIn">
					  """	
		
	res_17_keys = res_17.keys()
	if res_17_keys:
		for key in res_17_keys:
			html_link = '"'+res_17[key]+'"'
			message+="""<div id="res_17" class="wrap_class">
								<p><a href="""+html_link+""" class="showLink" target="_blank">
									  Click Here For server Details """+key+"""
								  </a>
								</p>
							</div>"""
			
	else :
		message+="""<div id="res_17_else" class="wrap_class">
							<table style="width:100%"><tr><td><h5></h5></td></tr>
							<tr><td><p><font size="3" color="Black"> No Server found For IMDIRSERVSEC </font></p></td></tr></table>
						</div>
						"""
		
	message+="""</div>
				</li>
				</ul>
				</body>
				</html>"""
				
	return message
	
	
def gen_mta_html(res_1,key):
	message = message_header
	message += """ 
				<body>
					<br><br>"""
	eth_cap_keys = res_1["ethernet_capacity"].keys()
	div_id = "'mta_"+key+"'"
	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>MTA Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""
	message_key+=process_line(res_1,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" </p></td></tr>"""
		for line in res_1["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
		message_key+=process_line(res_1,"ethernet_capacity")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_1["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>MTA Version : </h5></td></tr>"""

	message_key+=process_line(res_1,"mx_version")
	message_key+= """</table>"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_1,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_1["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_1["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_1["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_1["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_1["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_1["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_1["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_1["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_1["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_1,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_1,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_1,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_1,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_1,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_1,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_1,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_1,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_1,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_1,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_1,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_1,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_1,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_1,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_1,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_1,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_1,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_1,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_1,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_1,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_1,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_1,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_1,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_1,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_1,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_1,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_1,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_1,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_1,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	if res_1.has_key('spool_dir_data'):
		message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Spool Directory Info : </h5></td></tr>"""

		message_key+=process_line(res_1,"spool_dir_data")
		message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_1,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_1["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_1["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_1,"nic_card_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_1,"cifsiostat_data")	
	
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_1,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_1,"netstat_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_1,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>"""
	return message
	
def gen_imap_html(res_2,key):
	message = message_header
	message += """
				<body>
					<br><br>"""
	eth_cap_keys = res_2["ethernet_capacity"].keys()
	div_id = "'imap_"+key+"'"
	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>IMAP Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_2,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" </p></td></tr>"""
		for line in res_2["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_2["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>IMAP Version : </h5></td></tr>"""

	message_key+=process_line(res_2,"mx_version")
	message_key+= """</table>"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_2,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_2["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_2["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_2["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_2["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_2["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	
						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_2["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_2["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_2["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_2["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_2,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_2,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_2,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_2,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_2,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_2,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_2,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_2,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_2,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_2,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_2,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_2,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_2,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_2,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_2,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_2,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_2,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_2,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_2,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_2,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_2,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_2,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_2,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_2,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_2,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_2,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_2,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_2,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_2,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_2,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_2["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_2["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_2,"nic_card_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_2,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_2,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_2,"netstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_2,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_pop_html(res_3,key):
	message = message_header
	message += """ 
				<body>
					<br><br>"""
	eth_cap_keys = res_3["ethernet_capacity"].keys()
	div_id = "'pop_"+key+"'"
	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>POP Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_3,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_3["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_3["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>POP Version : </h5></td></tr>"""

	message_key+=process_line(res_3,"mx_version")
	message_key+= """</table>"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_3,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_3["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_3["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_3["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_3["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_3["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_3["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_3["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_3["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_3["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_3,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_3,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_3,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_3,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_3,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_3,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_3,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_3,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_3,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_3,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_3,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_3,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_3,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_3,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_3,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_3,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_3,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_3,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_3,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_3,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_3,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_3,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_3,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_3,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_3,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_3,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_3,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_3,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_3,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	if res_3.has_key('spool_dir_data'):
		message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Spool Directory Info : </h5></td></tr>"""

		message_key+=process_line(res_3,"spool_dir_data")
		message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_3,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_3["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_3["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_3,"nic_card_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_3,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_3,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_3,"netstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_3,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_mss_html(res_4,key):
	message = message_header
	message += """ 
			<body>
					<br><br>"""
	eth_cap_keys = res_4["ethernet_capacity"].keys()
	div_id = "'mss_"+key+"'"
	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>MSS Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_4,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_4["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_4["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>MSS Version : </h5></td></tr>"""

	message_key+=process_line(res_4,"mx_version")
	message_key+= """</table>"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_4,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_4["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_4["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_4["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_4["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_4["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_4["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_4["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_4["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_4["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_4,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_4,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_4,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_4,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_4,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_4,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_4,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_4,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_4,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_4,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_4,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_4,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_4,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_4,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_4,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_4,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_4,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_4,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_4,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_4,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_4,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_4,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_4,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_4,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_4,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_4,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_4,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_4,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_4,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	if res_4.has_key('spool_dir_data'):
		message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Spool Directory Info : </h5></td></tr>"""

		message_key+=process_line(res_4,"spool_dir_data")
		message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_4,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_4["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_4["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_4,"nic_card_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_4,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_4,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_4,"netstat_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_4,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_mxos_html(res_5,key):
	message = message_header
	message += """ 
				<body>
					<br><br>"""
					
	eth_cap_keys = res_5["ethernet_capacity"].keys()
	div_id = "'mxos_"+key+"'"
	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>MXOS Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Tomcat Version : </h5>
						</td>
					</tr>"""

	message_key+=process_line(res_5,"tomcat_data")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_5,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_5["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_5["kernel_version"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>MXOS Installation Status : </h5></td></tr>
					<tr><td><p>"""+res_5["mxos_install"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>MXOS Version : </h5></td></tr>"""

	message_key+=process_line(res_5,"mxos_version_info")
	message_key+= """</table>"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_5,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_5["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_5["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_5["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_5["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_5["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	
						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_5["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_5["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_5["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_5["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_5,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_5,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_5,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_5,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_5,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_5,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_5,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_5,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_5,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_5,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_5,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_5,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_5,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_5,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_5,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_5,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_5,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_5,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_5,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_5,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_5,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_5,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_5,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_5,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_5,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_5,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_5,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_5,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_5,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_5,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_5["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_5["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_5,"nic_card_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_5,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_5,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_5,"netstat_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_5,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
	
def gen_app_suite_html(res_6,key):
	message = message_header
	message += """ 
			<body>
					<br><br>"""
	
	dict_vals = res_6.keys()
	eth_cap_keys = res_6["ethernet_capacity"].keys()
	div_id = "'app_suite_"+key+"'"
	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>App Suite Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_6,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_6["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_6["kernel_version"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>HTTPD Status : </h5></td></tr>
					<tr><td><p>"""+res_6["httpd_status_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Open Xchange Status : </h5></td></tr>
					<tr><td><p>"""+res_6["open_xchange_status_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>MYSQLD Status : </h5></td></tr>
					<tr><td><p>"""+res_6["mysqld_status_info"]+"""</p></td></tr></table>
					
					</div>
					<div class="divClass">
					"""
	message_key+="""<table style="width:100%"><tr><td><h5>App Suite Status : </h5></td></tr>
					<tr><td><p>"""+res_6["app_suite_install"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>App Suite Version : </h5></td></tr>
					<tr><td><p>"""+res_6["app_suite_version"]+"""</p></td></tr></table>"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_6,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_6["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	

	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_6["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_6["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_6["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_6["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	
						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_6["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_6["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_6["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_6["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_6,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_6,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_6,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_6,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_6,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_6,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_6,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_6,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_6,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_6,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_6,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_6,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_6,"rlogin_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_6,"rlogin_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_6,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_6,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_6,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_6,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_6,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_6,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_6,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_6,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_6,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_6,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_6,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_6,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_6,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_6,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_6,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_6,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_6["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_6["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_6,"nic_card_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_6,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_6,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_6,"netstat_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_6,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_cass_meta_html(res_7,key):
	message = message_header
	message += """ 
			<body>
					<br><br>"""
	dict_vals = res_7.keys()
	eth_cap_keys = res_7["ethernet_capacity"].keys()
	div_id = "'cass_meta_"+key+"'"

	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>Cassandra Meta Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_7,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_7["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_7["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					"""
			
	message_key+="""<table style="width:100%"><tr><td><h5>Cassandra Version : </h5></td></tr>
					<tr><td><p>"""+res_7["cassandra_version"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Cassandra Ring Status : </h5></td></tr>
					<tr><td><p>"""+res_7["cassandra_ring_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_7,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_7["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_7["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_7["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_7["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_7["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	
						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_7["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_7["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_7["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_7["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_7,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_7,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_7,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_7,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_7,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_7,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_7,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_7,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_7,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_7,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_7,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_7,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_7,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_7,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_7,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_7,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_7,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_7,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_7,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_7,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_7,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_7,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_7,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_7,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_7,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_7,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_7,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_7,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_7,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_7,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_7["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_7["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_7,"nic_card_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_7,"cifsiostat_data")
		
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_7,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_7,"netstat_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_7,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_cass_blob_html(res_8,key):
	message = message_header
	message += """
			<body>
					<br><br>"""
	dict_vals = res_8.keys()
	eth_cap_keys = res_8["ethernet_capacity"].keys()
	div_id = "'cass_blob_"+key+"'"

	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>Cassandra Blob Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_8,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_8["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_8["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					"""
			
	message_key+="""<table style="width:100%"><tr><td><h5>Cassandra Version : </h5></td></tr>
					<tr><td><p>"""+res_8["cassandra_version"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Cassandra Ring Status : </h5></td></tr>
					<tr><td><p>"""+res_8["cassandra_ring_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_8,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_8["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_8["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_8["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_8["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_8["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	
						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_8["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_8["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_8["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_8["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_8,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_8,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_8,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_8,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_8,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_8,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_8,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_8,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_8,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_8,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_8,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_8,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_8,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_8,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_8,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_8,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_8,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_8,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_8,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_8,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_8,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_8,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_8,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_8,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_8,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_8,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_8,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_8,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_8,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_8,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_8["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_8["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_8,"nic_card_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_8,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_8,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_8,"netstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_8,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_mysqldb_html(res_9,key):
	message = message_header
	message += """
				<body>
					<br><br>"""
	dict_vals = res_9.keys()
	eth_cap_keys = res_9["ethernet_capacity"].keys()
	div_id = "'mysqldb_"+key+"'"
	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>MYSQLDB Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_9,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_9["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_9["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					"""
			
	message_key+="""<table style="width:100%"><tr><td><h5>MYSQL DB Version : </h5></td></tr>
					<tr><td><p>"""+res_9["mysqldb_version"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_9,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_9["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_9["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_9["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_9["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_9["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	
						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_9["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_9["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_9["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_9["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_9,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_9,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_9,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_9,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_9,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_9,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_9,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_9,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_9,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_9,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_9,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_9,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_9,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_9,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_9,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_9,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_9,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_9,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_9,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_9,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_9,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_9,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_9,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_9,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_9,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_9,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_9,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_9,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_9,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_9,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_9["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_9["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_9,"nic_card_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_9,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_9,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_9,"netstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_9,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message

def gen_nginx_html(res_10,key):
	message = message_header
	message += """
			<body>
					<br><br>"""
	dict_vals = res_10.keys()
	eth_cap_keys = res_10["ethernet_capacity"].keys()
	div_id = "'nginx_"+key+"'"

	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>NGINX Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_10,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_10["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_10["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_10,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_10["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_10["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_10["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_10["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_10["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	
						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_10["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_10["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_10["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_10["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_10,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_10,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_10,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_10,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_10,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_10,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_10,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_10,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_10,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_10,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_10,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_10,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_10,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_10,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_10,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_10,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_10,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_10,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_10,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_10,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_10,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_10,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_10,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_10,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_10,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_10,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_10,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_10,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_10,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_10,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_10["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_10["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_10,"nic_card_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_10,"cifsiostat_data")
		
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_10,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_10,"netstat_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_10,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_imqueueserv_html(res_11,key):
	message = message_header
	message += """ 
			<body>
					<br><br>"""
	dict_vals = res_11.keys()
	eth_cap_keys = res_11["ethernet_capacity"].keys()
	div_id = "'imqueueserv_"+key+"'"

	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>IMQUEUESERV Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_11,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_11["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_11["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_11,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_11["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_11["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_11["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_11["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_11["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	
						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_11["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_11["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_11["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_11["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_11,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_11,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_11,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_11,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_11,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_11,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_11,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_11,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_11,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_11,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_11,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_11,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_11,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_11,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_11,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_11,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_11,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_11,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_11,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_11,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_11,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_11,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_11,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_11,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_11,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_11,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_11,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_11,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_11,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_11,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_11["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_11["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_11,"nic_card_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_11,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_11,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_11,"netstat_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_11,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_imextserv_html(res_12,key):
	message = message_header
	message += """
			<body>
					<br><br>"""
	dict_vals = res_12.keys()
	eth_cap_keys = res_12["ethernet_capacity"].keys()
	div_id = "'imextserv_"+key+"'"

	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>IMEXTSERV Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_12,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_12["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_12["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_12,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_12["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_12["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_12["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_12["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_12["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	
						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_12["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_12["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_12["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_12["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_12,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_12,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_12,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_12,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_12,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_12,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_12,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_12,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_12,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_12,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_12,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_12,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_12,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_12,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_12,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_12,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_12,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_12,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_12,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_12,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_12,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_12,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_12,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_12,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_12,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_12,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_12,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_12,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_12,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_12,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_12["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_12["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_12,"nic_card_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_12,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_12,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_12,"netstat_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_12,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_imdirserv_html(res_13,key):
	message = message_header
	message += """
			<body>
					<br><br>"""
	dict_vals = res_13.keys()
	eth_cap_keys = res_13["ethernet_capacity"].keys()
	div_id = "'imdirserv_"+key+"'"
	# div_id = "'"+key+"'"
	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>IMDIRSERV Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_13,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_13["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_13["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_13,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_13["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_13["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_13["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_13["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_13["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	
						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_13["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_13["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_13["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_13["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_13,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_13,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_13,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_13,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_13,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_13,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_13,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_13,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_13,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_13,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_13,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_13,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_13,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_13,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_13,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_13,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_13,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_13,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_13,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_13,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_13,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_13,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_13,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_13,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_13,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_13,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_13,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_13,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_13,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_13,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_13["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_13["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_13,"nic_card_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_13,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_13,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_13,"netstat_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_13,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_immgrserv_html(res_14,key):
	message = message_header
	message += """
				<body>
					<br><br>"""
	dict_vals = res_14.keys()
	eth_cap_keys = res_14["ethernet_capacity"].keys()
	div_id = "'immgrserv_"+key+"'"

	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>IMMGRSERV Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_14,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_14["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_14["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_14,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_14["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						
	
	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_14["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_14["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_14["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_14["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""
	
						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_14["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_14["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_14["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_14["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_14,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_14,"disk_size")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_14,"running_mod_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_14,"cpu_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_14,"memory_info")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_14,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_14,"process_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_14,"sysctl_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_14,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_14,"SeLinux_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_14,"ntp_version")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_14,"rlogin_status")
	message_key+= """</table></div>"""
	
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_14,"ssh_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_14,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_14,"ftp_status")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_14,"sar_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_14,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_14,"mpstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_14,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_14,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_14,"w_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_14,"getent_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_14,"system_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_14,"ss_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_14,"list_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_14,"list_groups")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_14,"profile_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_14,"admin_users")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_14,"mounted_devices_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_14,"interface_data")
	message_key+= """</table>"""
	
	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_14["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_14["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_14,"nic_card_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_14,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_14,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_14,"netstat_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_14,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_imconfserv_html(res_15,key):
	message = message_header
	message += """
				<body>
					<br><br>"""
	dict_vals = res_15.keys()
	eth_cap_keys = res_15["ethernet_capacity"].keys()
	div_id = "'imconfserv_"+key+"'"

	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>IMCONFSERV Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_15,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_15["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_15["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_15,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_15["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						

	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_15["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_15["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_15["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_15["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""

						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_15["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_15["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_15["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_15["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_15,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_15,"disk_size")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_15,"running_mod_info")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_15,"cpu_info")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_15,"memory_info")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_15,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_15,"process_status")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_15,"sysctl_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_15,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_15,"SeLinux_status")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_15,"ntp_version")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_15,"rlogin_status")
	message_key+= """</table></div>"""


	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_15,"ssh_status")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_15,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_15,"ftp_status")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_15,"sar_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_15,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_15,"mpstat_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_15,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_15,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_15,"w_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_15,"getent_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_15,"system_users")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_15,"ss_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_15,"list_users")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_15,"list_groups")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_15,"profile_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_15,"admin_users")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_15,"mounted_devices_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_15,"interface_data")
	message_key+= """</table>"""

	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_15["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_15["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_15,"nic_card_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_15,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_15,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_15,"netstat_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_15,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_imdircacheserv_html(res_16,key):
	message = message_header
	message += """
			<body>
					<br><br>"""
	dict_vals = res_16.keys()
	eth_cap_keys = res_16["ethernet_capacity"].keys()
	div_id = "'imdircacheserv_"+key+"'"

	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>IMDIRCACHESERV Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_16,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_16["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_16["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_16,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_16["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						

	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_16["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_16["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_16["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_16["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""

						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_16["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_16["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_16["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_16["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_16,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_16,"disk_size")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_16,"running_mod_info")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_16,"cpu_info")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_16,"memory_info")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_16,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_16,"process_status")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_16,"sysctl_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_16,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_16,"SeLinux_status")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_16,"ntp_version")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_16,"ntp_version")
	message_key+= """</table></div>"""


	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_16,"ssh_status")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_16,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_16,"ftp_status")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_16,"sar_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_16,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_16,"mpstat_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_16,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_16,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_16,"w_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_16,"getent_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_16,"system_users")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_16,"ss_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_16,"list_users")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_16,"list_groups")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_16,"profile_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_16,"admin_users")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_16,"mounted_devices_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_16,"interface_data")
	message_key+= """</table>"""

	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_16["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_16["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_16,"nic_card_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_16,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_16,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_16,"netstat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_16,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key
	
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
	
def gen_imdirservsec_html(res_17,key):
	message = message_header
	message += """
			<body>
					<br><br>"""
	dict_vals = res_17.keys()
	eth_cap_keys = res_17["ethernet_capacity"].keys()
	div_id = "'IMDIRSERVSEC_"+key+"'"

	message_key = """
					<div id="wrap">
					<div id="""+div_id+""">
					<div class="heading">
					<h3>IMDIRSERVSEC Server """+key+""" </h3>
					</div>
					<div class="divClass">
					<table style="width:100%"><tr><td><h5>Ethernet Driver : </h5></td></tr>"""

	message_key+=process_line(res_17,"ethernet_driver")
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Ethernet Driver Capacity : </h5></td></tr>"""
	for eth_key in eth_cap_keys:
		message_key+="""<tr><td><p>"""
		message_key+=eth_key+""" :- </p></td></tr>"""
		for line in res_17["ethernet_capacity"][eth_key]:
			message_key+="""<tr><td><p>"""
			message_key+=line
			message_key+= """</p></td></tr>"""
	message_key+= """</table>
					<table style="width:100%"><tr><td><h5>Kernel Version : </h5></td></tr>
					<tr><td><p>"""+res_17["kernel_version"]+"""</p></td></tr></table>
					</div>
					<div class="divClass">
					"""
			
	message_key+="""<table style="width:100%"><tr><td>
					<h5>RHEL Version : </h5></td></tr>"""

	message_key+=process_line(res_17,"rhel_version_info")
	message_key+= """</table>"""
					
	message_key+="""<table style="width:100%"><tr><td><h5>IRQBalance Version : </h5></td></tr>
					<tr><td><p>"""+res_17["irqbalance_version"]+"""</p></td></tr></table>
					</div>"""						

	message_key+="""<div class="divClass">
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of soft Files : </h5>
						</td>
					</tr>
					<tr><td>
					<p>"""+res_17["ulimit_soft_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%">
					<tr>
						<td>
					<h5>Ulimit no. of Hard Files : </h5>
						</td>
					</tr>
					<tr><td><p>"""+res_17["ulimit_hard_no_files"]+"""</p>
						</td>
					</tr>
					</table>
					<table style="width:100%"><tr><td><h5>RPM Count : </h5></td></tr>
					<tr><td><p>"""+res_17["rpm_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5> Count of Open Files : </h5></td></tr>
					<tr><td><p>"""+res_17["lsof_count"]+"""</p></td></tr></table>
					</div>
					"""

						  
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Date Time And Timezone Data : </h5></td></tr>
					<tr><td><p>"""+res_17["date_time_timezone_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>SCP Status : </h5></td></tr>
					<tr><td><p>"""+res_17["scp_status"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UPTIME Output. : </h5></td></tr>
					<tr><td><p>"""+res_17["uptime_data"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>  UName -a Output. : </h5></td></tr>
				  <tr><td><p>"""+res_17["uname_data"]+"""</p></td></tr></table>
					</div>
					"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Number of Disk's Information : </h5></td></tr>"""

	message_key+=process_line(res_17,"no_of_disks")
	message_key+= """</table></div>"""
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Disk Size Information : </h5></td></tr>"""

	message_key+=process_line(res_17,"disk_size")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Running Modules : </h5></td></tr>"""

	message_key+=process_line(res_17,"running_mod_info")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>CPU Information : </h5></td></tr>"""

	message_key+=process_line(res_17,"cpu_info")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Memory Information : </h5></td></tr>"""

	message_key+=process_line(res_17,"memory_info")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>RPM List Information : </h5></td></tr>"""

	message_key+=process_line(res_17,"rpm_list_info")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td>
					<h5>Process Status : </h5></td></tr>"""

	message_key+=process_line(res_17,"process_status")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Sysctl Data : </h5></td></tr>"""

	message_key+=process_line(res_17,"sysctl_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>chkconfig Enabled Services : </h5></td></tr>"""

	message_key+=process_line(res_17,"chkconfig_enabled_services")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SeLinux Status : </h5></td></tr>"""

	message_key+=process_line(res_17,"SeLinux_status")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>NTP Version : </h5></td></tr>"""

	message_key+=process_line(res_17,"ntp_version")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>rlogin Service Status : </h5></td></tr>"""

	message_key+=process_line(res_17,"rlogin_status")
	message_key+= """</table></div>"""


	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SSH Service Status : </h5></td></tr>"""

	message_key+=process_line(res_17,"ssh_status")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Telnet Service Status : </h5></td></tr>"""

	message_key+=process_line(res_17,"telnet_status")
	message_key+= """</table>"""
		
	message_key+="""<table style="width:100%"><tr><td><h5>FTP Service Status : </h5></td></tr>"""

	message_key+=process_line(res_17,"ftp_status")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>SAR utility data for system's real Time Performance : </h5></td></tr>"""

	message_key+=process_line(res_17,"sar_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CPU, disk I/O, and NFS statistics : </h5></td></tr>"""

	message_key+=process_line(res_17,"iostat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Processors Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_17,"mpstat_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Virtual Memory Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_17,"vmstat_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Physical (RAM) and Swap Memory of your system. : </h5></td></tr>"""

	message_key+=process_line(res_17,"free_mem_data")
	message_key+= """</table></div>"""
		
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Users currently on the machine and their Processes : </h5></td></tr>"""

	message_key+=process_line(res_17,"w_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>To see who is in groups root, wheel adm and admin : </h5></td></tr>"""

	message_key+=process_line(res_17,"getent_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>System Users : </h5></td></tr>"""

	message_key+=process_line(res_17,"system_users")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Socket Statistics. : </h5></td></tr>"""

	message_key+=process_line(res_17,"ss_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Users : </h5></td></tr>"""

	message_key+=process_line(res_17,"list_users")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>List of all Groups : </h5></td></tr>"""

	message_key+=process_line(res_17,"list_groups")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>.Profile Data : </h5></td></tr>"""

	message_key+=process_line(res_17,"profile_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Administrator users and Users with administrative rights : </h5></td></tr>"""

	message_key+=process_line(res_17,"admin_users")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Mounted Devices Data : </h5></td></tr>"""

	message_key+=process_line(res_17,"mounted_devices_data")
	message_key+= """</table></div>"""

	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Interface Data : </h5></td></tr>"""

	message_key+=process_line(res_17,"interface_data")
	message_key+= """</table>"""

	message_key+="""<table style="width:100%"><tr><td><h5>IPTables Validations : </h5></td></tr>
					<tr><td><p>"""+res_17["iptables_info"]+"""</p></td></tr></table>
					<table style="width:100%"><tr><td><h5>Java Version : </h5></td></tr>
					<tr><td><p>"""+res_17["java_version_info"]+"""</p></td></tr></table>
					</div>			  
				"""
				
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Interface Card Data : </h5></td></tr>"""

	message_key+=process_line(res_17,"nic_card_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>CIFS file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_17,"cifsiostat_data")
	message_key+="""<table style="width:100%"><tr><td><h5>NFS mounted file system's Read and Write Data : </h5></td></tr>"""

	message_key+=process_line(res_17,"nfsiostat_data")
	message_key+= """</table></div>"""
	
	message_key+="""<div class="divClass"><table style="width:100%"><tr><td><h5>Network Connections on system: </h5></td></tr>"""

	message_key+=process_line(res_17,"netstat_data")
	message_key+= """</table></div>"""
				
	message_key+="""<div class="log_div_Class2"><table style="width:100%"><tr><td><h5>List of Open Files : </h5></td></tr>"""

	message_key+=process_line(res_17,"lsof_list")
	message_key+= """</table></div>"""
	message_key+= """</div></div>"""
	message+=message_key		
	
	
	message+=""" </div>
				</li>
				</ul>
				</body>
				</html>
					  """
	return message
