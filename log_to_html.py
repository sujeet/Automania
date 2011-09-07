from Constants import *

def css () :
    return """ <style type = text/css>                                                          
     .metacontainer {                                                                 
         -moz-border-radius    :	10px;                                             
         -webkit-border-radius :	10px;                                             
         -moz-box-shadow       :	5px 5px 7px #555555;                              
         -webkit-box-shadow    :	5px 5px 7px #555555;                              
         width                 :	 """ + str ((MAP_SIZE - 1)*10 + 210)+ """px;             
         height                :	 """ + str ((MAP_SIZE - 1)*10) + """px;                   
         margin                :	 0pt auto;                                        
         padding               :	 20px 10px 20px 20px;                                            
         border                :	 0pt none;                                        
         background            :	 none repeat scroll 0% 0% """ + BKG_COLOUR + """;   
     }                                                                                
     .legend {                                                                        
         width                 :	 200px;                                           
         -moz-border-radius    :	10px;                                             
         -webkit-border-radius :	10px;                                             
         float                 :    right;                                            
         margin                :	 10px 0 0;                              
         background            :	 none repeat scroll 0% 0% """ + EMPTY_COLOUR + """; 
     }                                                                                
     .status {                                                                        
         width                 :	 200px;                                           
         -moz-border-radius    :	10px;                                             
         -webkit-border-radius :	10px;                                             
         float                 :	 right;                                           
         margin                :	 10px 0 0;                                        
         background            :	 none repeat scroll 0% 0% """ + EMPTY_COLOUR + """; 
     }                                                                                
     .control {                                                              
         width                 :	 200px;                                           
         -moz-border-radius    :	10px;                                             
         -webkit-border-radius :	10px;                                             
         float                 :	 right;                                           
         margin                :	 0;                                        
         background            :	 none repeat scroll 0% 0% """ + EMPTY_COLOUR + """; 
     }                                                                                
     .point_number {                                                                  
         text-align            :	 right;                                           
     }                                                                                
     button {                                                                         
         width                 :	 100%;                                            
     }                                                                                
     .container{                                                                      
         margin                :	 0pt;                                             
         padding               :	 0pt;                                             
         float                 :	 left;                                            
         border                :	 thin solid #aaaaaa;
         background            :	 none repeat scroll 0% 0% """ + EMPTY_COLOUR + """; 
     }

     .black {                                                                                                                
     	color                 : #d7d7d7;                                                                                     
     	border                : solid 1px #333;                                                                              
     	background            : #333;                                                                                        
     	background            : -webkit-gradient(linear, left top, left bottom, from(#666), to(#000));                       
     	background            : -moz-linear-gradient(top,  #666,  #000);                                                     
     	filter                :  progid:DXImageTransform.Microsoft.gradient(startColorstr='#666666', endColorstr='#000000'); 
     }                                                                                                                       
     .black:hover {                                                                                                          
     	background            : #000;                                                                                        
     	background            : -webkit-gradient(linear, left top, left bottom, from(#444), to(#000));                       
     	background            : -moz-linear-gradient(top,  #444,  #000);                                                     
     	filter                :  progid:DXImageTransform.Microsoft.gradient(startColorstr='#444444', endColorstr='#000000'); 
     }                                                                                                                       
     .black:active {                                                                                                         
     	color                 : #666;                                                                                        
     	background            : -webkit-gradient(linear, left top, left bottom, from(#000), to(#444));                       
     	background            : -moz-linear-gradient(top,  #000,  #444);                                                     
     	filter                :  progid:DXImageTransform.Microsoft.gradient(startColorstr='#000000', endColorstr='#666666'); 
     }                                                                                                                       
                                                                                                                             
     .button {                                                                                                               
     	display               : inline-block;                                                                                
     	zoom                  : 1; /* zoom and *display = ie7 hack for display:inline-block */                               
     	*display              : inline;                                                                                      
     	vertical-align        : baseline;                                                                                    
     	margin                : 0 2px;                                                                                       
     	width                 : 50px;                                                                                      
     	outline               : none;                                                                                        
     	cursor                : pointer;                                                                                     
     	text-align            : center;                                                                                      
     	text-decoration       : none;                                                                                        
     	font                  : 14px/100% Arial, Helvetica, sans-serif;                                                      
     	padding               : 5px;                                                                                         
     	text-shadow           : 0 1px 1px rgba(0,0,0,.3);                                                                    
     	-webkit-border-radius : .5em;                                                                                        
     	-moz-border-radius    : .5em;                                                                                        
     	border-radius         : .5em;                                                                                        
     	-webkit-box-shadow    : 0 1px 2px rgba(0,0,0,.2);                                                                    
     	-moz-box-shadow       : 0 1px 2px rgba(0,0,0,.2);                                                                    
     	box-shadow            : 0 1px 2px rgba(0,0,0,.2);                                                                    
     }                                                                                                                       
     .button:hover {                                                                                                         
     	text-decoration       : none;                                                                                        
     }                                                                                                                       
     .button:active {                                                                                                        
     	position              : relative;                                                                                    
     	top                   : 1px;                                                                                         
     }
     </style> """                                                                                                                      

def legend () :
      return """<div class='legend'>                                                                   
      <table style='width: 200px; border-spacing: 10px; color: """ + TEXT_COLOUR + """;'>      
          <tbody><tr>                                                                        
              <th colspan='2'> Legend </th>                                                  
          </tr>                                                                              
          <tr>                                                                               
          </tr>                                                                              
          <tr>                                                                               
              <td>                                                                           
                  <canvas id='""" + BIKE_1_SYMBOL + """' height=10px width=10px></canvas>              
              </td>                                                                          
              <td> Player one bike                                                           
              </td>                                                                          
          </tr>                                                                              
          <tr>                                                                               
              <td>                                                                           
                  <canvas id='""" + BIKE_2_SYMBOL + """' height=10px width=10px></canvas>              
              </td>                                                                          
              <td> Player two bike                                                           
              </td>                                                                          
          </tr>                                                                              
          <tr>                                                                               
              <td>                                                                           
                  <canvas id='""" + WALL + """' height=10px width=10px></canvas>               
              </td>                                                                          
              <td> Wall                                                                      
              </td>                                                                          
          </tr>                                                                              
          <tr>                                                                               
          </tr>                                                                              
          <tr>                                                                               
          </tr>                                                                              
          <tr>                                                                               
              <td>                                                                           
                  <canvas id='""" + NITRO + """' height=10px width=10px></canvas>               
              </td>                                                                          
              <td> Nitro power
              </td>                                                                          
          </tr>                                                                              
          <tr>                                                                               
              <td>                                                                           
                  <canvas id='""" + TRAVERSER + """' height=10px width=10px></canvas>               
              </td>                                                                          
              <td> Traverser power
              </td>                                                                          
          </tr>                                                                              
          <tr>                                                                               
              <td>                                                                           
                  <canvas id='""" + RESET + """' height=10px width=10px></canvas>               
              </td>                                                                          
              <td> Reset power
              </td>                                                                          
          </tr>                                                                              
      </tbody></table>                                                                       
      </div>""" 

def canvas () :
    return """<canvas id = 'container' class = 'container' width = '""" + str ((MAP_SIZE-1)*10) + """' height = '""" + str ((MAP_SIZE-1)*10) + """'></canvas>"""

def status_notifier () :
    return """<div class ='status'>                                                                                            
      <table style='width: 200px; color: """ + TEXT_COLOUR + """;'>                                                      
          <tr>                                                                                                         
              <td>                                                                                                     
                 <span style = 'font-weight : bold'> Moves :</span>                                                    
              </td>                                                                                                    
              <td> <div id='number_of_moves'> 0 </div> </td>                                                           
          </tr>                                                                                                        
      </table>                                                                                                         
      </div> """

def controls () :
    return """ <div class ='control'>                                                                       
      <table style='width: 200px; border-spacing: 10px; color: """ + TEXT_COLOUR + """;'>                
          <tr>                                                                                         
              <th colspan='3'> Controls </th>                                                          
          </tr>                                                                                        
          <tr>                                                                                         
              <td>                                                                                     
                  <button id='step_backward' class='button black' >                                    
                     &lt;&lt;                                                                          
                  </button>                                                                            
              </td>                                                                                    
              <td>                                                                                     
                  <button id='pause_button' class='button black' onclick='pause_game()'>               
                      Play                                                                             
                  </button>                                                                            
              </td>                                                                                    
              <td>                                                                                     
                  <button id='step_forward' class='button black'>                                      
                      &gt;&gt;                                                                         
                  </button>                                                                            
              </td>                                                                                    
          </tr>                                                                                        
          <tr>                                                                                         
              <td>                                                                       
                  <button id='slow_button' class='button black' style='padding-left:2px' onclick='slow()'>                      
                      Slower                                                                           
                  </button>                                                                            
              </td>                                                                                    
              <td>                                                                       
                  <button id='restart_button' class='button black' style='padding-left:2px' onclick='window.location.reload()'> 
                      Reload
                  </button>                                                                            
              </td>                                                                                    
              <td>                                                                       
                  <button id='fast_button' class='button black' style='padding-left:3px' onclick='fast()'>                      
                      Faster                                                                           
                  </button>                                                                            
              </td>                                                                                    
          </tr>                                                                                        
      </table>                                                                                         
      </div> """                                                                                           

def diff_array () :
    logfile = open (LOG_FILE)
    lines = logfile.readlines ()
    logfile.close ()
    string_to_return = "var diff_array = [["

    i = 0
    for line in lines :
        x, y, old_symbol, new_symbol = line.strip().split (" ")
        if (old_symbol != END_SCORE_CHAR) :
            string_to_return += "[" + x + "," + y + ",'" + old_symbol + "','" + new_symbol + "'],"
        else :
            # Last array contains scores.
            string_to_return += "[" + x + "," + y + "]],["
            i += 1

    string_to_return += "]];"
    string_to_return += "var max_number_of_funcs = " + str (i) + ";"

    return string_to_return

    
def js () :
    string_to_return = "<script type='text/javascript'>"

        # Global variabrles for js
    string_to_return += """ var pause = true;                                  
        var function_counter = 1;                          
        var delay = """ + str (DELAY) + """;                       
        var delay_step = """ + str (DELAY_STEP) + """;             
        var min_delay = """ + str (MIN_DELAY) + """;               
        var max_delay = """ + str (MAX_DELAY) + """;               
        var x;                                             
        var y;                                             
        var canvas = document.getElementById('container'); 
        var ctx = canvas.getContext('2d');"""

    # Function to draw the blast when the bot is dead.
    string_to_return += """ function drawStar(ctx,r, x, y, color, spikes){   
        ctx.save();                                  
        ctx.beginPath();                             
        ctx.translate (x, y);                        
        ctx.fillStyle = color;                       
        ctx.moveTo(r,0);                             
        for (var i=0;i<( 2*spikes - 1 );i++){        
            ctx.rotate(Math.PI/spikes);              
            if(i%2 == 0) {                           
                ctx.lineTo((r/0.525731)*0.200811,0); 
            } else {                                 
                ctx.lineTo(r,0);                     
            }                                        
        }                                            
        ctx.closePath();                             
        ctx.fill();                                  
        ctx.restore();                               
             } """                                                

    # Function to fill out the canvas at appropriate places.
    string_to_return += """ function fill_the_canvas (x, y, name)                   
            {                                                       
               switch (name)                                        
               {                                                    
                   case '""" + DEAD_SYMBOL + """' :                          
                       drawStar(ctx, 10, x + 5, y + 5, 'red', 7);   
                       drawStar(ctx, 6, x + 5, y + 5, 'yellow', 7); 
                       break;                                       
                                                                    
                   case '""" + WALL + """' :                          
                       ctx.fillStyle = '""" + WALL_COLOUR + """';     
                       ctx.fillRect (x, y, 10, 10);                 
                       break;                                       
                                                                    
                   case '""" + EMPTY + """' :                         
                       ctx.fillStyle = '""" + EMPTY_COLOUR + """';    
                       ctx.fillRect (x, y, 10, 10);                 
                       break;                                       
                                                                    
                   case '""" + GOLD + """' :                          
                       ctx.fillStyle = 'rgba(256, 220, 0, 0.5)';    
                       ctx.fillRect (x, y, 10, 10);                 
                       ctx.fillStyle = 'rgba(256, 220, 0, 1)';      
                       ctx.fillRect (x+2, y+2, 6, 6);               
                       break;                                       
                                                                    
                   case '""" + BUNKER1 + """' :                       
                       ctx.fillStyle = 'rgba(0, 256, 0, 0.2)';      
                       ctx.fillRect (x, y, 10, 10);                 
                       break;                                       
                                                                    
                   case '""" + BUNKER2 + """' :                       
                       ctx.fillStyle = 'rgba(256, 0, 0, 0.2)';      
                       ctx.fillRect (x, y, 10, 10);                 
                       break;                                       
                                                                    
                   case '""" + BIKE_1_SYMBOL + """' :                         
                       ctx.fillStyle = 'rgba(0, 256, 0, 0.5)';      
                       ctx.fillRect (x, y, 10, 10);                 
                       ctx.fillStyle = 'rgba(0, 256, 0, 1)';        
                       ctx.fillRect (x+2, y+2, 6, 6);               
                       break;                                       
                                                                    
                   case '""" + BIKE_2_SYMBOL + """' :                         
                       ctx.fillStyle = 'rgba(256, 0, 0, 0.5)';      
                       ctx.fillRect (x, y, 10, 10);                 
                       ctx.fillStyle = 'rgba(256, 0, 0, 1)';        
                       ctx.fillRect (x+2, y+2, 6, 6);               
                       break;                                       
                                                                    
                   case '""" + RESET + """' :                   
                       ctx.fillStyle = 'rgba(0, 256, 256, 0.5)';    
                       ctx.fillRect (x, y, 10, 10);                 
                       ctx.fillStyle = 'rgba(0, 256, 256, 1)';      
                       ctx.fillRect (x+2, y+2, 6, 6);               
                       break;                                       
                                                                    
                   case '""" + BULLET1 + """' :                       
                       ctx.fillStyle = 'rgba(256, 256, 256, 0.5)';  
                       ctx.fillRect (x+3, y+3, 4, 4);               
                       ctx.fillStyle = 'rgba(256, 256, 256, 1)';    
                       ctx.fillRect (x+4, y+4, 2, 2);               
                       break;                                       
                                                                    
                   case '""" + BULLET2 + """' :                       
                       ctx.fillStyle = 'rgba(256, 256, 256, 0.5)';  
                       ctx.fillRect (x+3, y+3, 4, 4);               
                       ctx.fillStyle = 'rgba(256, 256, 256, 1)';    
                       ctx.fillRect (x+4, y+4, 2, 2);               
                       break;                                       
                                                                    
                   case '""" + RESET_BULLET + """' :            
                       ctx.fillStyle = 'rgba(256, 256, 256, 0.5)';  
                       ctx.fillRect (x+3, y+3, 4, 4);               
                       ctx.fillStyle = 'rgba(256, 256, 256, 1)';    
                       ctx.fillRect (x+4, y+4, 2, 2);               
                       break;                                       
                                                                    
                   case '""" + NITRO + """' :                       
                       ctx.fillStyle = '""" + NITRO_COLOUR + """';  
                       ctx.beginPath();                             
                       ctx.arc(x+5, y+5, 5, 0, Math.PI*2, true);    
                       ctx.closePath();                             
                       ctx.fill();                                  
                       break;                                       
                                                                    
                   case '""" + TRAVERSER + """' :                       
                       ctx.fillStyle = '""" + TRAVERSER_COLOUR + """';  
                       ctx.beginPath();                             
                       ctx.arc(x+5, y+5, 5, 0, Math.PI*2, true);    
                       ctx.closePath();                             
                       ctx.fill();                                  
                       break;                                       
               }                                                    
            } """                                                        

    # Fill the legend with small canvases.
    string_to_return += """ 
            canvas = document.getElementById('""" + BIKE_1_SYMBOL + """');              
            ctx = canvas.getContext('2d');                                    
            fill_the_canvas (0, 0, '""" + BIKE_1_SYMBOL + """');                        
            canvas = document.getElementById('""" + BIKE_2_SYMBOL + """');              
            ctx = canvas.getContext('2d');                                    
            fill_the_canvas (0, 0, '""" + BIKE_2_SYMBOL + """');                        
            canvas = document.getElementById('""" + WALL + """');               
            ctx = canvas.getContext('2d');                                    
            fill_the_canvas (0, 0, '""" + WALL + """');
            canvas = document.getElementById('""" + NITRO + """');               
            ctx = canvas.getContext('2d');                                    
            fill_the_canvas (0, 0, '""" + NITRO + """');
            canvas = document.getElementById('""" + TRAVERSER + """');               
            ctx = canvas.getContext('2d');                                    
            fill_the_canvas (0, 0, '""" + TRAVERSER + """');
            canvas = document.getElementById('""" + RESET + """');               
            ctx = canvas.getContext('2d');                                    
            fill_the_canvas (0, 0, '""" + RESET + """');
            """
    
    # Set the canvas and ctx back.
    string_to_return += """ canvas = document.getElementById('container'); 
            ctx = canvas.getContext('2d'); """                 
    
    # Now insert the diff array.
    string_to_return += diff_array ()

    # Function to print stuff on map.
    string_to_return += """ function update_map (turn_number)                                                        
            {                                                                                        
                 var i = 0;                                                                          
                 for (i = 0; i < diff_array[turn_number].length - 1; i++){                           
                      var y = diff_array[turn_number][i][0];                                         
                      var x = diff_array[turn_number][i][1];                                         
                      var symbol_to_display = diff_array[turn_number][i][3];                         
                      fill_the_canvas (x*10, y*10, symbol_to_display);                               
                 }                                                                                   
            }"""

    # Function to go back.
    string_to_return += """ function go_back (turn_number)                                                           
            {                                                                                        
                 var i = diff_array[turn_number].length - 1;                                         
                 for (i = diff_array[turn_number].length - 2; i >=0; i--){                           
                      var y = diff_array[turn_number][i][0];                                         
                      var x = diff_array[turn_number][i][1];                                         
                      var symbol_to_display = diff_array[turn_number][i][2];                         
                      fill_the_canvas (x*10, y*10, symbol_to_display);                               
                 }                                                                                   
            }"""                                                                                        

    # Functions to step back and forward.
    string_to_return += """ function step_back ()                                                     
            {                                                                         
                 if (function_counter == 0) {                                         
                     function_counter = max_number_of_funcs - 1;                      
                 }                                                                    
                 go_back (function_counter);                                          
                 function_counter--;                                                  
            }                                                                         

    function step_forward ()                                                  
            {                                                                         
                 update_map (function_counter);                                       
                 function_counter++;                                                  
                 function_counter = function_counter % max_number_of_funcs;           
            }"""
    
    # Now the play function
    string_to_return += """ function play()                                                                 
            {                                                                               
               if (function_counter >= max_number_of_funcs) {                               
                   pause_game ();                                                           
                   function_counter = function_counter % max_number_of_funcs;               
                   return;                                                                  
               }                                                                            
               if (! pause) {                                                               
                   update_map(function_counter);                                            
                   document.getElementById('number_of_moves').innerHTML = function_counter; 
                   function_counter = function_counter + 1;                                 
                   var t = setTimeout ('play()', delay);                                    
               }                                                                            
               else {                                                                       
                   return;                                                                  
               }                                                                            
            }                                                                               

    function pause_game()                                                    
            {                                                                        
                pause = ! pause;                                                     
                document.getElementById('pause_button').innerHTML = 'Play';          
                document.getElementById('step_forward').style.display = 'block';     
                document.getElementById('step_backward').style.display = 'block';    
                if ( ! pause ) {                                                     
                    play();                                                          
                    document.getElementById('pause_button').innerHTML = 'Pause';     
                    document.getElementById('step_forward').style.display = 'none';  
                    document.getElementById('step_backward').style.display = 'none'; 
                }                                                                    
            }                                                                        

    function fast()                                             
            {                                                           
                if (delay >= min_delay) {                               
                    delay -= delay_step;                                
                }                                                       
            }                                                           
                                                                            
    function slow()                                             
            {                                                           
                if (delay <= max_delay) {                               
                    delay += delay_step;                                
                }                                                       
            }"""                                                           

    # This function creates a closure and puts a mousedown handler on the element specified in the 'button' parameter.  
    string_to_return += """ function makeButtonIncrement(button, action, initialDelay){                                                         
                    var holdTimer, changeValue, timerIsRunning = false, delay = initialDelay;                                   
                    changeValue = function(){                                                                                   
                            if(action == 'forward' && function_counter < max_number_of_funcs)                                   
                                step_forward();                                                                                 
                            else if(action == 'backward' && function_counter >= 0)                                              
                                step_back();                                                                                    
                            holdTimer = setTimeout(changeValue, delay);                                                         
                            if(!timerIsRunning){                                                                                
                                    // When the function is first called, it puts an onmouseup handler on the whole document    
                                    // that stops the process when the mouse is released. This is important if the user moves   
                                    // the cursor off of the button.                                                            
                                    document.onmouseup = function(){                                                            
                                            clearTimeout(holdTimer);                                                            
                                            document.onmouseup = null;                                                          
                                            timerIsRunning = false;                                                             
                                            delay = initialDelay;                                                               
                                    }                                                                                           
                                    timerIsRunning = true;                                                                      
                            }                                                                                                   
                    }                                                                                                           
                    button.onmousedown = changeValue;                                                                           
            }                                                                                                                   
                                                                                                                                
            // should only be called after the window/DOM has been loaded                                                        
            window.onload = function() {                                                                                        
                    makeButtonIncrement(document.getElementById('step_forward'), 'forward', 100);                               
                    makeButtonIncrement(document.getElementById('step_backward'), 'backward', 100);                             
            }; """                                                                                                                   
    # Now call the function to paint initially.
    string_to_return += """ update_map (0);"""

    string_to_return += """ </script> """

    return string_to_return


if __name__ == "__main__" :
    html_file = open (HTML_FILE, 'w')
    html = ("<html><head>"
            + css ()
            + """</head>
            <body style='background:#aaaaaa;'>
            <div class = 'metacontainer'>"""
            + canvas ()
            + controls ()
            + status_notifier ()
            + legend ()
            + "</div>"
            + js ()
            + "</body></html>")
    html_file.write (html)
    html_file.close ()
    
