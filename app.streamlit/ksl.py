from PIL import Image
import streamlit as st


st.set_page_config(page_title="KSQUARE LOGISTICS SOLUTION", page_icon=":tada:", layout="wide")
#-----load assets-----#
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        local_css("style/style.css")
        
#----HEADER----#
img_KSL_theme = Image.open("images/KSL_theme.png")
with st.container():
    image_column, text_column = st.columns((20,1))
    with image_column:
        st.image(img_KSL_theme)
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("LINKING BETTER")     
# ----CONTACT----
with st.container():
    st.write("---")
    st.header("GET QUOTED HERE!")
    st.write("##")


    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/ksquare.logs@gmail.com" method="POST">
    <head>
    <style>
    /* CSS Snippet from W3schools: https://www.w3schools.com/howto/howto_css_contact_form.asp */
/* Style inputs with type="text", select elements and textareas */
input[type=email], input[type=text], textarea {
    width: 100%; /* Full width */
    padding: 12px; /* Some padding */ 
    border: 1px solid #ccc; /* Gray border */
    border-radius: 4px; /* Rounded borders */
    box-sizing: border-box; /* Make sure that padding and width stays in place */
    margin-top: 6px; /* Add a top margin */
    margin-bottom: 16px; /* Bottom margin */
    resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
  }
  @font-face {
    font-family: 'FontAwesome';
    src: url('fonts/fontawesome-webfont.eot?v=4.5.0');
    src: url('fonts/fontawesome-webfont.eot?#iefix&v=4.5.0') format('embedded-opentype'), url('fonts/fontawesome-webfont.woff2?v=4.5.0') format('woff2'), url('fonts/fontawesome-webfont.woff?v=4.5.0') format('woff'), url('fonts/fontawesome-webfont.ttf?v=4.5.0') format('truetype'), url('fonts/fontawesome-webfont.svg?v=4.5.0#fontawesomeregular') format('svg');
    font-weight: normal;
    font-style: normal;
  }
  .fa {
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  /* makes the font 33% larger relative to the icon container */
  .fa-lg {
    font-size: 1.33333333em;
    line-height: 0.75em;
    vertical-align: -15%;
  }
  .fa-2x {
    font-size: 2em;
  }
  .fa-3x {
    font-size: 3em;
  }
  .fa-4x {
    font-size: 4em;
  }
  .fa-5x {
    font-size: 5em;
  }
  .fa-fw {
    width: 1.28571429em;
    text-align: center;
  }
  .fa-ul {
    padding-left: 0;
    margin-left: 2.14285714em;
    list-style-type: none;
  }
  .fa-ul > li {
    position: relative;
  }
  .fa-li {
    position: absolute;
    left: -2.14285714em;
    width: 2.14285714em;
    top: 0.14285714em;
    text-align: center;
  }
  .fa-li.fa-lg {
    left: -1.85714286em;
  }
  .fa-border {
    padding: .2em .25em .15em;
    border: solid 0.08em #eeeeee;
    border-radius: .1em;
  }
  .fa-pull-left {
    float: left;
  }
  .fa-pull-right {
    float: right;
  }
  .fa.fa-pull-left {
    margin-right: .3em;
  }
  .fa.fa-pull-right {
    margin-left: .3em;
  }
  /* Deprecated as of 4.4.0 */
  .pull-right {
    float: right;
  }
  .pull-left {
    float: left;
  }
  .fa.pull-left {
    margin-right: .3em;
  }
  .fa.pull-right {
    margin-left: .3em;
  }
  .fa-spin {
    -webkit-animation: fa-spin 2s infinite linear;
    animation: fa-spin 2s infinite linear;
  }
  .fa-pulse {
    -webkit-animation: fa-spin 1s infinite steps(8);
    animation: fa-spin 1s infinite steps(8);
  }
  @-webkit-keyframes fa-spin {
    0% {
      -webkit-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(359deg);
      transform: rotate(359deg);
    }
  }
  @keyframes fa-spin {
    0% {
      -webkit-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(359deg);
      transform: rotate(359deg);
    }
  }
  .fa-rotate-90 {
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
    -webkit-transform: rotate(90deg);
    -ms-transform: rotate(90deg);
    transform: rotate(90deg);
  }
  .fa-rotate-180 {
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
    -webkit-transform: rotate(180deg);
    -ms-transform: rotate(180deg);
    transform: rotate(180deg);
  }
  .fa-rotate-270 {
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
    -webkit-transform: rotate(270deg);
    -ms-transform: rotate(270deg);
    transform: rotate(270deg);
  }
  .fa-flip-horizontal {
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);
    -webkit-transform: scale(-1, 1);
    -ms-transform: scale(-1, 1);
    transform: scale(-1, 1);
  }
  .fa-flip-vertical {
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);
    -webkit-transform: scale(1, -1);
    -ms-transform: scale(1, -1);
    transform: scale(1, -1);
  }
  :root .fa-rotate-90,
  :root .fa-rotate-180,
  :root .fa-rotate-270,
  :root .fa-flip-horizontal,
  :root .fa-flip-vertical {
    filter: none;
  }
  .fa-stack {
    position: relative;
    display: inline-block;
    width: 2em;
    height: 2em;
    line-height: 2em;
    vertical-align: middle;
  }
  .fa-stack-1x,
  .fa-stack-2x {
    position: absolute;
    left: 0;
    width: 100%;
    text-align: center;
  }
  .fa-stack-1x {
    line-height: inherit;
  }
  .fa-stack-2x {
    font-size: 2em;
  }
  .fa-inverse {
    color: #ffffff;
  }
  /* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
     readers do not read off random characters that represent icons */
  .fa-glass:before {
    content: "\f000";
  }
  .fa-music:before {
    content: "\f001";
  }
  .fa-search:before {
    content: "\f002";
  }
  .fa-envelope-o:before {
    content: "\f003";
  }
  .fa-heart:before {
    content: "\f004";
  }
  .fa-star:before {
    content: "\f005";
  }
  .fa-star-o:before {
    content: "\f006";
  }
  .fa-user:before {
    content: "\f007";
  }
  .fa-film:before {
    content: "\f008";
  }
  .fa-th-large:before {
    content: "\f009";
  }
  .fa-th:before {
    content: "\f00a";
  }
  .fa-th-list:before {
    content: "\f00b";
  }
  .fa-check:before {
    content: "\f00c";
  }
  .fa-remove:before,
  .fa-close:before,
  .fa-times:before {
    content: "\f00d";
  }
  .fa-search-plus:before {
    content: "\f00e";
  }
  .fa-search-minus:before {
    content: "\f010";
  }
  .fa-power-off:before {
    content: "\f011";
  }
  .fa-signal:before {
    content: "\f012";
  }
  .fa-gear:before,
  .fa-cog:before {
    content: "\f013";
  }
  .fa-trash-o:before {
    content: "\f014";
  }
  .fa-home:before {
    content: "\f015";
  }
  .fa-file-o:before {
    content: "\f016";
  }
  .fa-clock-o:before {
    content: "\f017";
  }
  .fa-road:before {
    content: "\f018";
  }
  .fa-download:before {
    content: "\f019";
  }
  .fa-arrow-circle-o-down:before {
    content: "\f01a";
  }
  .fa-arrow-circle-o-up:before {
    content: "\f01b";
  }
  .fa-inbox:before {
    content: "\f01c";
  }
  .fa-play-circle-o:before {
    content: "\f01d";
  }
  .fa-rotate-right:before,
  .fa-repeat:before {
    content: "\f01e";
  }
  .fa-refresh:before {
    content: "\f021";
  }
  .fa-list-alt:before {
    content: "\f022";
  }
  .fa-lock:before {
    content: "\f023";
  }
  .fa-flag:before {
    content: "\f024";
  }
  .fa-headphones:before {
    content: "\f025";
  }
  .fa-volume-off:before {
    content: "\f026";
  }
  .fa-volume-down:before {
    content: "\f027";
  }
  .fa-volume-up:before {
    content: "\f028";
  }
  .fa-qrcode:before {
    content: "\f029";
  }
  .fa-barcode:before {
    content: "\f02a";
  }
  .fa-tag:before {
    content: "\f02b";
  }
  .fa-tags:before {
    content: "\f02c";
  }
  .fa-book:before {
    content: "\f02d";
  }
  .fa-bookmark:before {
    content: "\f02e";
  }
  .fa-print:before {
    content: "\f02f";
  }
  .fa-camera:before {
    content: "\f030";
  }
  .fa-font:before {
    content: "\f031";
  }
  .fa-bold:before {
    content: "\f032";
  }
  .fa-italic:before {
    content: "\f033";
  }
  .fa-text-height:before {
    content: "\f034";
  }
  .fa-text-width:before {
    content: "\f035";
  }
  .fa-align-left:before {
    content: "\f036";
  }
  .fa-align-center:before {
    content: "\f037";
  }
  .fa-align-right:before {
    content: "\f038";
  }
  .fa-align-justify:before {
    content: "\f039";
  }
  .fa-list:before {
    content: "\f03a";
  }
  .fa-dedent:before,
  .fa-outdent:before {
    content: "\f03b";
  }
  .fa-indent:before {
    content: "\f03c";
  }
  .fa-video-camera:before {
    content: "\f03d";
  }
  .fa-photo:before,
  .fa-image:before,
  .fa-picture-o:before {
    content: "\f03e";
  }
  .fa-pencil:before {
    content: "\f040";
  }
  .fa-map-marker:before {
    content: "\f041";
  }
  .fa-adjust:before {
    content: "\f042";
  }
  .fa-tint:before {
    content: "\f043";
  }
  .fa-edit:before,
  .fa-pencil-square-o:before {
    content: "\f044";
  }
  .fa-share-square-o:before {
    content: "\f045";
  }
  .fa-check-square-o:before {
    content: "\f046";
  }
  .fa-arrows:before {
    content: "\f047";
  }
  .fa-step-backward:before {
    content: "\f048";
  }
  .fa-fast-backward:before {
    content: "\f049";
  }
  .fa-backward:before {
    content: "\f04a";
  }
  .fa-play:before {
    content: "\f04b";
  }
  .fa-pause:before {
    content: "\f04c";
  }
  .fa-stop:before {
    content: "\f04d";
  }
  .fa-forward:before {
    content: "\f04e";
  }
  .fa-fast-forward:before {
    content: "\f050";
  }
  .fa-step-forward:before {
    content: "\f051";
  }
  .fa-eject:before {
    content: "\f052";
  }
  .fa-chevron-left:before {
    content: "\f053";
  }
  .fa-chevron-right:before {
    content: "\f054";
  }
  .fa-plus-circle:before {
    content: "\f055";
  }
  .fa-minus-circle:before {
    content: "\f056";
  }
  .fa-times-circle:before {
    content: "\f057";
  }
  .fa-check-circle:before {
    content: "\f058";
  }
  .fa-question-circle:before {
    content: "\f059";
  }
  .fa-info-circle:before {
    content: "\f05a";
  }
  .fa-crosshairs:before {
    content: "\f05b";
  }
  .fa-times-circle-o:before {
    content: "\f05c";
  }
  .fa-check-circle-o:before {
    content: "\f05d";
  }
  .fa-ban:before {
    content: "\f05e";
  }
  .fa-arrow-left:before {
    content: "\f060";
  }
  .fa-arrow-right:before {
    content: "\f061";
  }
  .fa-arrow-up:before {
    content: "\f062";
  }
  .fa-arrow-down:before {
    content: "\f063";
  }
  .fa-mail-forward:before,
  .fa-share:before {
    content: "\f064";
  }
  .fa-expand:before {
    content: "\f065";
  }
  .fa-compress:before {
    content: "\f066";
  }
  .fa-plus:before {
    content: "\f067";
  }
  .fa-minus:before {
    content: "\f068";
  }
  .fa-asterisk:before {
    content: "\f069";
  }
  .fa-exclamation-circle:before {
    content: "\f06a";
  }
  .fa-gift:before {
    content: "\f06b";
  }
  .fa-leaf:before {
    content: "\f06c";
  }
  .fa-fire:before {
    content: "\f06d";
  }
  .fa-eye:before {
    content: "\f06e";
  }
  .fa-eye-slash:before {
    content: "\f070";
  }
  .fa-warning:before,
  .fa-exclamation-triangle:before {
    content: "\f071";
  }
  .fa-plane:before {
    content: "\f072";
  }
  .fa-calendar:before {
    content: "\f073";
  }
  .fa-random:before {
    content: "\f074";
  }
  .fa-comment:before {
    content: "\f075";
  }
  .fa-magnet:before {
    content: "\f076";
  }
  .fa-chevron-up:before {
    content: "\f077";
  }
  .fa-chevron-down:before {
    content: "\f078";
  }
  .fa-retweet:before {
    content: "\f079";
  }
  .fa-shopping-cart:before {
    content: "\f07a";
  }
  .fa-folder:before {
    content: "\f07b";
  }
  .fa-folder-open:before {
    content: "\f07c";
  }
  .fa-arrows-v:before {
    content: "\f07d";
  }
  .fa-arrows-h:before {
    content: "\f07e";
  }
  .fa-bar-chart-o:before,
  .fa-bar-chart:before {
    content: "\f080";
  }
  .fa-twitter-square:before {
    content: "\f081";
  }
  .fa-facebook-square:before {
    content: "\f082";
  }
  .fa-camera-retro:before {
    content: "\f083";
  }
  .fa-key:before {
    content: "\f084";
  }
  .fa-gears:before,
  .fa-cogs:before {
    content: "\f085";
  }
  .fa-comments:before {
    content: "\f086";
  }
  .fa-thumbs-o-up:before {
    content: "\f087";
  }
  .fa-thumbs-o-down:before {
    content: "\f088";
  }
  .fa-star-half:before {
    content: "\f089";
  }
  .fa-heart-o:before {
    content: "\f08a";
  }
  .fa-sign-out:before {
    content: "\f08b";
  }
  .fa-linkedin-square:before {
    content: "\f08c";
  }
  .fa-thumb-tack:before {
    content: "\f08d";
  }
  .fa-external-link:before {
    content: "\f08e";
  }
  .fa-sign-in:before {
    content: "\f090";
  }
  .fa-trophy:before {
    content: "\f091";
  }
  .fa-github-square:before {
    content: "\f092";
  }
  .fa-upload:before {
    content: "\f093";
  }
  .fa-lemon-o:before {
    content: "\f094";
  }
  .fa-phone:before {
    content: "\f095";
  }
  .fa-square-o:before {
    content: "\f096";
  }
  .fa-bookmark-o:before {
    content: "\f097";
  }
  .fa-phone-square:before {
    content: "\f098";
  }
  .fa-twitter:before {
    content: "\f099";
  }
  .fa-facebook-f:before,
  .fa-facebook:before {
    content: "\f09a";
  }
  .fa-github:before {
    content: "\f09b";
  }
  .fa-unlock:before {
    content: "\f09c";
  }
  .fa-credit-card:before {
    content: "\f09d";
  }
  .fa-feed:before,
  .fa-rss:before {
    content: "\f09e";
  }
  .fa-hdd-o:before {
    content: "\f0a0";
  }
  .fa-bullhorn:before {
    content: "\f0a1";
  }
  .fa-bell:before {
    content: "\f0f3";
  }
  .fa-certificate:before {
    content: "\f0a3";
  }
  .fa-hand-o-right:before {
    content: "\f0a4";
  }
  .fa-hand-o-left:before {
    content: "\f0a5";
  }
  .fa-hand-o-up:before {
    content: "\f0a6";
  }
  .fa-hand-o-down:before {
    content: "\f0a7";
  }
  .fa-arrow-circle-left:before {
    content: "\f0a8";
  }
  .fa-arrow-circle-right:before {
    content: "\f0a9";
  }
  .fa-arrow-circle-up:before {
    content: "\f0aa";
  }
  .fa-arrow-circle-down:before {
    content: "\f0ab";
  }
  .fa-globe:before {
    content: "\f0ac";
  }
  .fa-wrench:before {
    content: "\f0ad";
  }
  .fa-tasks:before {
    content: "\f0ae";
  }
  .fa-filter:before {
    content: "\f0b0";
  }
  .fa-briefcase:before {
    content: "\f0b1";
  }
  .fa-arrows-alt:before {
    content: "\f0b2";
  }
  .fa-group:before,
  .fa-users:before {
    content: "\f0c0";
  }
  .fa-chain:before,
  .fa-link:before {
    content: "\f0c1";
  }
  .fa-cloud:before {
    content: "\f0c2";
  }
  .fa-flask:before {
    content: "\f0c3";
  }
  .fa-cut:before,
  .fa-scissors:before {
    content: "\f0c4";
  }
  .fa-copy:before,
  .fa-files-o:before {
    content: "\f0c5";
  }
  .fa-paperclip:before {
    content: "\f0c6";
  }
  .fa-save:before,
  .fa-floppy-o:before {
    content: "\f0c7";
  }
  .fa-square:before {
    content: "\f0c8";
  }
  .fa-navicon:before,
  .fa-reorder:before,
  .fa-bars:before {
    content: "\f0c9";
  }
  .fa-list-ul:before {
    content: "\f0ca";
  }
  .fa-list-ol:before {
    content: "\f0cb";
  }
  .fa-strikethrough:before {
    content: "\f0cc";
  }
  .fa-underline:before {
    content: "\f0cd";
  }
  .fa-table:before {
    content: "\f0ce";
  }
  .fa-magic:before {
    content: "\f0d0";
  }
  .fa-truck:before {
    content: "\f0d1";
  }
  .fa-pinterest:before {
    content: "\f0d2";
  }
  .fa-pinterest-square:before {
    content: "\f0d3";
  }
  .fa-google-plus-square:before {
    content: "\f0d4";
  }
  .fa-google-plus:before {
    content: "\f0d5";
  }
  .fa-money:before {
    content: "\f0d6";
  }
  .fa-caret-down:before {
    content: "\f0d7";
  }
  .fa-caret-up:before {
    content: "\f0d8";
  }
  .fa-caret-left:before {
    content: "\f0d9";
  }
  .fa-caret-right:before {
    content: "\f0da";
  }
  .fa-columns:before {
    content: "\f0db";
  }
  .fa-unsorted:before,
  .fa-sort:before {
    content: "\f0dc";
  }
  .fa-sort-down:before,
  .fa-sort-desc:before {
    content: "\f0dd";
  }
  .fa-sort-up:before,
  .fa-sort-asc:before {
    content: "\f0de";
  }
  .fa-envelope:before {
    content: "\f0e0";
  }
  .fa-linkedin:before {
    content: "\f0e1";
  }
  .fa-rotate-left:before,
  .fa-undo:before {
    content: "\f0e2";
  }
  .fa-legal:before,
  .fa-gavel:before {
    content: "\f0e3";
  }
  .fa-dashboard:before,
  .fa-tachometer:before {
    content: "\f0e4";
  }
  .fa-comment-o:before {
    content: "\f0e5";
  }
  .fa-comments-o:before {
    content: "\f0e6";
  }
  .fa-flash:before,
  .fa-bolt:before {
    content: "\f0e7";
  }
  .fa-sitemap:before {
    content: "\f0e8";
  }
  .fa-umbrella:before {
    content: "\f0e9";
  }
  .fa-paste:before,
  .fa-clipboard:before {
    content: "\f0ea";
  }
  .fa-lightbulb-o:before {
    content: "\f0eb";
  }
  .fa-exchange:before {
    content: "\f0ec";
  }
  .fa-cloud-download:before {
    content: "\f0ed";
  }
  .fa-cloud-upload:before {
    content: "\f0ee";
  }
  .fa-user-md:before {
    content: "\f0f0";
  }
  .fa-stethoscope:before {
    content: "\f0f1";
  }
  .fa-suitcase:before {
    content: "\f0f2";
  }
  .fa-bell-o:before {
    content: "\f0a2";
  }
  .fa-coffee:before {
    content: "\f0f4";
  }
  .fa-cutlery:before {
    content: "\f0f5";
  }
  .fa-file-text-o:before {
    content: "\f0f6";
  }
  .fa-cargo-lite-o:before {
    content: "\f0f7";
  }
  .fa-hospital-o:before {
    content: "\f0f8";
  }
  .fa-ambulance:before {
    content: "\f0f9";
  }
  .fa-medkit:before {
    content: "\f0fa";
  }
  .fa-fighter-jet:before {
    content: "\f0fb";
  }
  .fa-beer:before {
    content: "\f0fc";
  }
  .fa-h-square:before {
    content: "\f0fd";
  }
  .fa-plus-square:before {
    content: "\f0fe";
  }
  .fa-angle-double-left:before {
    content: "\f100";
  }
  .fa-angle-double-right:before {
    content: "\f101";
  }
  .fa-angle-double-up:before {
    content: "\f102";
  }
  .fa-angle-double-down:before {
    content: "\f103";
  }
  .fa-angle-left:before {
    content: "\f104";
  }
  .fa-angle-right:before {
    content: "\f105";
  }
  .fa-angle-up:before {
    content: "\f106";
  }
  .fa-angle-down:before {
    content: "\f107";
  }
  .fa-desktop:before {
    content: "\f108";
  }
  .fa-laptop:before {
    content: "\f109";
  }
  .fa-tablet:before {
    content: "\f10a";
  }
  .fa-mobile-phone:before,
  .fa-mobile:before {
    content: "\f10b";
  }
  .fa-circle-o:before {
    content: "\f10c";
  }
  .fa-quote-left:before {
    content: "\f10d";
  }
  .fa-quote-right:before {
    content: "\f10e";
  }
  .fa-spinner:before {
    content: "\f110";
  }
  .fa-circle:before {
    content: "\f111";
  }
  .fa-mail-reply:before,
  .fa-reply:before {
    content: "\f112";
  }
  .fa-github-alt:before {
    content: "\f113";
  }
  .fa-folder-o:before {
    content: "\f114";
  }
  .fa-folder-open-o:before {
    content: "\f115";
  }
  .fa-smile-o:before {
    content: "\f118";
  }
  .fa-frown-o:before {
    content: "\f119";
  }
  .fa-meh-o:before {
    content: "\f11a";
  }
  .fa-gamepad:before {
    content: "\f11b";
  }
  .fa-keyboard-o:before {
    content: "\f11c";
  }
  .fa-flag-o:before {
    content: "\f11d";
  }
  .fa-flag-checkered:before {
    content: "\f11e";
  }
  .fa-terminal:before {
    content: "\f120";
  }
  .fa-code:before {
    content: "\f121";
  }
  .fa-mail-reply-all:before,
  .fa-reply-all:before {
    content: "\f122";
  }
  .fa-star-half-empty:before,
  .fa-star-half-full:before,
  .fa-star-half-o:before {
    content: "\f123";
  }
  .fa-location-arrow:before {
    content: "\f124";
  }
  .fa-crop:before {
    content: "\f125";
  }
  .fa-code-fork:before {
    content: "\f126";
  }
  .fa-unlink:before,
  .fa-chain-broken:before {
    content: "\f127";
  }
  .fa-question:before {
    content: "\f128";
  }
  .fa-info:before {
    content: "\f129";
  }
  .fa-exclamation:before {
    content: "\f12a";
  }
  .fa-superscript:before {
    content: "\f12b";
  }
  .fa-subscript:before {
    content: "\f12c";
  }
  .fa-eraser:before {
    content: "\f12d";
  }
  .fa-puzzle-piece:before {
    content: "\f12e";
  }
  .fa-microphone:before {
    content: "\f130";
  }
  .fa-microphone-slash:before {
    content: "\f131";
  }
  .fa-shield:before {
    content: "\f132";
  }
  .fa-calendar-o:before {
    content: "\f133";
  }
  .fa-fire-extinguisher:before {
    content: "\f134";
  }
  .fa-rocket:before {
    content: "\f135";
  }
  .fa-maxcdn:before {
    content: "\f136";
  }
  .fa-chevron-circle-left:before {
    content: "\f137";
  }
  .fa-chevron-circle-right:before {
    content: "\f138";
  }
  .fa-chevron-circle-up:before {
    content: "\f139";
  }
  .fa-chevron-circle-down:before {
    content: "\f13a";
  }
  .fa-html5:before {
    content: "\f13b";
  }
  .fa-css3:before {
    content: "\f13c";
  }
  .fa-anchor:before {
    content: "\f13d";
  }
  .fa-unlock-alt:before {
    content: "\f13e";
  }
  .fa-bullseye:before {
    content: "\f140";
  }
  .fa-ellipsis-h:before {
    content: "\f141";
  }
  .fa-ellipsis-v:before {
    content: "\f142";
  }
  .fa-rss-square:before {
    content: "\f143";
  }
  .fa-play-circle:before {
    content: "\f144";
  }
  .fa-ticket:before {
    content: "\f145";
  }
  .fa-minus-square:before {
    content: "\f146";
  }
  .fa-minus-square-o:before {
    content: "\f147";
  }
  .fa-level-up:before {
    content: "\f148";
  }
  .fa-level-down:before {
    content: "\f149";
  }
  .fa-check-square:before {
    content: "\f14a";
  }
  .fa-pencil-square:before {
    content: "\f14b";
  }
  .fa-external-link-square:before {
    content: "\f14c";
  }
  .fa-share-square:before {
    content: "\f14d";
  }
  .fa-compass:before {
    content: "\f14e";
  }
  .fa-toggle-down:before,
  .fa-caret-square-o-down:before {
    content: "\f150";
  }
  .fa-toggle-up:before,
  .fa-caret-square-o-up:before {
    content: "\f151";
  }
  .fa-toggle-right:before,
  .fa-caret-square-o-right:before {
    content: "\f152";
  }
  .fa-euro:before,
  .fa-eur:before {
    content: "\f153";
  }
  .fa-gbp:before {
    content: "\f154";
  }
  .fa-dollar:before,
  .fa-usd:before {
    content: "\f155";
  }
  .fa-rupee:before,
  .fa-inr:before {
    content: "\f156";
  }
  .fa-cny:before,
  .fa-rmb:before,
  .fa-yen:before,
  .fa-jpy:before {
    content: "\f157";
  }
  .fa-ruble:before,
  .fa-rouble:before,
  .fa-rub:before {
    content: "\f158";
  }
  .fa-won:before,
  .fa-krw:before {
    content: "\f159";
  }
  .fa-bitcoin:before,
  .fa-btc:before {
    content: "\f15a";
  }
  .fa-file:before {
    content: "\f15b";
  }
  .fa-file-text:before {
    content: "\f15c";
  }
  .fa-sort-alpha-asc:before {
    content: "\f15d";
  }
  .fa-sort-alpha-desc:before {
    content: "\f15e";
  }
  .fa-sort-amount-asc:before {
    content: "\f160";
  }
  .fa-sort-amount-desc:before {
    content: "\f161";
  }
  .fa-sort-numeric-asc:before {
    content: "\f162";
  }
  .fa-sort-numeric-desc:before {
    content: "\f163";
  }
  .fa-thumbs-up:before {
    content: "\f164";
  }
  .fa-thumbs-down:before {
    content: "\f165";
  }
  .fa-youtube-square:before {
    content: "\f166";
  }
  .fa-youtube:before {
    content: "\f167";
  }
  .fa-xing:before {
    content: "\f168";
  }
  .fa-xing-square:before {
    content: "\f169";
  }
  .fa-youtube-play:before {
    content: "\f16a";
  }
  .fa-dropbox:before {
    content: "\f16b";
  }
  .fa-stack-overflow:before {
    content: "\f16c";
  }
  .fa-instagram:before {
    content: "\f16d";
  }
  .fa-flickr:before {
    content: "\f16e";
  }
  .fa-adn:before {
    content: "\f170";
  }
  .fa-bitbucket:before {
    content: "\f171";
  }
  .fa-bitbucket-square:before {
    content: "\f172";
  }
  .fa-tumblr:before {
    content: "\f173";
  }
  .fa-tumblr-square:before {
    content: "\f174";
  }
  .fa-long-arrow-down:before {
    content: "\f175";
  }
  .fa-long-arrow-up:before {
    content: "\f176";
  }
  .fa-long-arrow-left:before {
    content: "\f177";
  }
  .fa-long-arrow-right:before {
    content: "\f178";
  }
  .fa-apple:before {
    content: "\f179";
  }
  .fa-windows:before {
    content: "\f17a";
  }
  .fa-android:before {
    content: "\f17b";
  }
  .fa-linux:before {
    content: "\f17c";
  }
  .fa-dribbble:before {
    content: "\f17d";
  }
  .fa-skype:before {
    content: "\f17e";
  }
  .fa-foursquare:before {
    content: "\f180";
  }
  .fa-trello:before {
    content: "\f181";
  }
  .fa-female:before {
    content: "\f182";
  }
  .fa-male:before {
    content: "\f183";
  }
  .fa-gittip:before,
  .fa-gratipay:before {
    content: "\f184";
  }
  .fa-sun-o:before {
    content: "\f185";
  }
  .fa-moon-o:before {
    content: "\f186";
  }
  .fa-archive:before {
    content: "\f187";
  }
  .fa-bug:before {
    content: "\f188";
  }
  .fa-vk:before {
    content: "\f189";
  }
  .fa-weibo:before {
    content: "\f18a";
  }
  .fa-renren:before {
    content: "\f18b";
  }
  .fa-pagelines:before {
    content: "\f18c";
  }
  .fa-stack-exchange:before {
    content: "\f18d";
  }
  .fa-arrow-circle-o-right:before {
    content: "\f18e";
  }
  .fa-arrow-circle-o-left:before {
    content: "\f190";
  }
  .fa-toggle-left:before,
  .fa-caret-square-o-left:before {
    content: "\f191";
  }
  .fa-dot-circle-o:before {
    content: "\f192";
  }
  .fa-wheelchair:before {
    content: "\f193";
  }
  .fa-vimeo-square:before {
    content: "\f194";
  }
  .fa-turkish-lira:before,
  .fa-try:before {
    content: "\f195";
  }
  .fa-plus-square-o:before {
    content: "\f196";
  }
  .fa-space-shuttle:before {
    content: "\f197";
  }
  .fa-slack:before {
    content: "\f198";
  }
  .fa-envelope-square:before {
    content: "\f199";
  }
  .fa-wordpress:before {
    content: "\f19a";
  }
  .fa-openid:before {
    content: "\f19b";
  }
  .fa-institution:before,
  .fa-bank:before,
  .fa-university:before {
    content: "\f19c";
  }
  .fa-mortar-board:before,
  .fa-graduation-cap:before {
    content: "\f19d";
  }
  .fa-yahoo:before {
    content: "\f19e";
  }
  .fa-google:before {
    content: "\f1a0";
  }
  .fa-reddit:before {
    content: "\f1a1";
  }
  .fa-reddit-square:before {
    content: "\f1a2";
  }
  .fa-stumbleupon-circle:before {
    content: "\f1a3";
  }
  .fa-stumbleupon:before {
    content: "\f1a4";
  }
  .fa-delicious:before {
    content: "\f1a5";
  }
  .fa-digg:before {
    content: "\f1a6";
  }
  .fa-pied-piper:before {
    content: "\f1a7";
  }
  .fa-pied-piper-alt:before {
    content: "\f1a8";
  }
  .fa-drupal:before {
    content: "\f1a9";
  }
  .fa-joomla:before {
    content: "\f1aa";
  }
  .fa-language:before {
    content: "\f1ab";
  }
  .fa-fax:before {
    content: "\f1ac";
  }
  .fa-cargo-lite:before {
    content: "\f1ad";
  }
  .fa-child:before {
    content: "\f1ae";
  }
  .fa-paw:before {
    content: "\f1b0";
  }
  .fa-spoon:before {
    content: "\f1b1";
  }
  .fa-cube:before {
    content: "\f1b2";
  }
  .fa-cubes:before {
    content: "\f1b3";
  }
  .fa-behance:before {
    content: "\f1b4";
  }
  .fa-behance-square:before {
    content: "\f1b5";
  }
  .fa-steam:before {
    content: "\f1b6";
  }
  .fa-steam-square:before {
    content: "\f1b7";
  }
  .fa-recycle:before {
    content: "\f1b8";
  }
  .fa-automobile:before,
  .fa-car:before {
    content: "\f1b9";
  }
  .fa-cab:before,
  .fa-taxi:before {
    content: "\f1ba";
  }
  .fa-tree:before {
    content: "\f1bb";
  }
  .fa-spotify:before {
    content: "\f1bc";
  }
  .fa-deviantart:before {
    content: "\f1bd";
  }
  .fa-soundcloud:before {
    content: "\f1be";
  }
  .fa-database:before {
    content: "\f1c0";
  }
  .fa-file-pdf-o:before {
    content: "\f1c1";
  }
  .fa-file-word-o:before {
    content: "\f1c2";
  }
  .fa-file-excel-o:before {
    content: "\f1c3";
  }
  .fa-file-powerpoint-o:before {
    content: "\f1c4";
  }
  .fa-file-photo-o:before,
  .fa-file-picture-o:before,
  .fa-file-image-o:before {
    content: "\f1c5";
  }
  .fa-file-zip-o:before,
  .fa-file-archive-o:before {
    content: "\f1c6";
  }
  .fa-file-sound-o:before,
  .fa-file-audio-o:before {
    content: "\f1c7";
  }
  .fa-file-movie-o:before,
  .fa-file-video-o:before {
    content: "\f1c8";
  }
  .fa-file-code-o:before {
    content: "\f1c9";
  }
  .fa-vine:before {
    content: "\f1ca";
  }
  .fa-codepen:before {
    content: "\f1cb";
  }
  .fa-jsfiddle:before {
    content: "\f1cc";
  }
  .fa-life-bouy:before,
  .fa-life-buoy:before,
  .fa-life-saver:before,
  .fa-support:before,
  .fa-life-ring:before {
    content: "\f1cd";
  }
  .fa-circle-o-notch:before {
    content: "\f1ce";
  }
  .fa-ra:before,
  .fa-rebel:before {
    content: "\f1d0";
  }
  .fa-ge:before,
  .fa-empire:before {
    content: "\f1d1";
  }
  .fa-git-square:before {
    content: "\f1d2";
  }
  .fa-git:before {
    content: "\f1d3";
  }
  .fa-y-combinator-square:before,
  .fa-yc-square:before,
  .fa-hacker-news:before {
    content: "\f1d4";
  }
  .fa-tencent-weibo:before {
    content: "\f1d5";
  }
  .fa-qq:before {
    content: "\f1d6";
  }
  .fa-wechat:before,
  .fa-weixin:before {
    content: "\f1d7";
  }
  .fa-send:before,
  .fa-paper-plane:before {
    content: "\f1d8";
  }
  .fa-send-o:before,
  .fa-paper-plane-o:before {
    content: "\f1d9";
  }
  .fa-history:before {
    content: "\f1da";
  }
  .fa-circle-thin:before {
    content: "\f1db";
  }
  .fa-header:before {
    content: "\f1dc";
  }
  .fa-paragraph:before {
    content: "\f1dd";
  }
  .fa-sliders:before {
    content: "\f1de";
  }
  .fa-share-alt:before {
    content: "\f1e0";
  }
  .fa-share-alt-square:before {
    content: "\f1e1";
  }
  .fa-bomb:before {
    content: "\f1e2";
  }
  .fa-soccer-ball-o:before,
  .fa-futbol-o:before {
    content: "\f1e3";
  }
  .fa-tty:before {
    content: "\f1e4";
  }
  .fa-binoculars:before {
    content: "\f1e5";
  }
  .fa-plug:before {
    content: "\f1e6";
  }
  .fa-slideshare:before {
    content: "\f1e7";
  }
  .fa-twitch:before {
    content: "\f1e8";
  }
  .fa-yelp:before {
    content: "\f1e9";
  }
  .fa-newspaper-o:before {
    content: "\f1ea";
  }
  .fa-wifi:before {
    content: "\f1eb";
  }
  .fa-calculator:before {
    content: "\f1ec";
  }
  .fa-paypal:before {
    content: "\f1ed";
  }
  .fa-google-wallet:before {
    content: "\f1ee";
  }
  .fa-cc-visa:before {
    content: "\f1f0";
  }
  .fa-cc-mastercard:before {
    content: "\f1f1";
  }
  .fa-cc-discover:before {
    content: "\f1f2";
  }
  .fa-cc-amex:before {
    content: "\f1f3";
  }
  .fa-cc-paypal:before {
    content: "\f1f4";
  }
  .fa-cc-stripe:before {
    content: "\f1f5";
  }
  .fa-bell-slash:before {
    content: "\f1f6";
  }
  .fa-bell-slash-o:before {
    content: "\f1f7";
  }
  .fa-trash:before {
    content: "\f1f8";
  }
  .fa-copyright:before {
    content: "\f1f9";
  }
  .fa-at:before {
    content: "\f1fa";
  }
  .fa-eyedropper:before {
    content: "\f1fb";
  }
  .fa-paint-brush:before {
    content: "\f1fc";
  }
  .fa-birthday-cake:before {
    content: "\f1fd";
  }
  .fa-area-chart:before {
    content: "\f1fe";
  }
  .fa-pie-chart:before {
    content: "\f200";
  }
  .fa-line-chart:before {
    content: "\f201";
  }
  .fa-lastfm:before {
    content: "\f202";
  }
  .fa-lastfm-square:before {
    content: "\f203";
  }
  .fa-toggle-off:before {
    content: "\f204";
  }
  .fa-toggle-on:before {
    content: "\f205";
  }
  .fa-bicycle:before {
    content: "\f206";
  }
  .fa-bus:before {
    content: "\f207";
  }
  .fa-ioxhost:before {
    content: "\f208";
  }
  .fa-angellist:before {
    content: "\f209";
  }
  .fa-cc:before {
    content: "\f20a";
  }
  .fa-shekel:before,
  .fa-sheqel:before,
  .fa-ils:before {
    content: "\f20b";
  }
  .fa-meanpath:before {
    content: "\f20c";
  }
  .fa-buysellads:before {
    content: "\f20d";
  }
  .fa-connectdevelop:before {
    content: "\f20e";
  }
  .fa-dashcube:before {
    content: "\f210";
  }
  .fa-forumbee:before {
    content: "\f211";
  }
  .fa-leanpub:before {
    content: "\f212";
  }
  .fa-sellsy:before {
    content: "\f213";
  }
  .fa-shirtsinbulk:before {
    content: "\f214";
  }
  .fa-simplybuilt:before {
    content: "\f215";
  }
  .fa-skyatlas:before {
    content: "\f216";
  }
  .fa-cart-plus:before {
    content: "\f217";
  }
  .fa-cart-arrow-down:before {
    content: "\f218";
  }
  .fa-diamond:before {
    content: "\f219";
  }
  .fa-ship:before {
    content: "\f21a";
  }
  .fa-user-secret:before {
    content: "\f21b";
  }
  .fa-motorcycle:before {
    content: "\f21c";
  }
  .fa-street-view:before {
    content: "\f21d";
  }
  .fa-heartbeat:before {
    content: "\f21e";
  }
  .fa-venus:before {
    content: "\f221";
  }
  .fa-mars:before {
    content: "\f222";
  }
  .fa-mercury:before {
    content: "\f223";
  }
  .fa-intersex:before,
  .fa-transgender:before {
    content: "\f224";
  }
  .fa-transgender-alt:before {
    content: "\f225";
  }
  .fa-venus-double:before {
    content: "\f226";
  }
  .fa-mars-double:before {
    content: "\f227";
  }
  .fa-venus-mars:before {
    content: "\f228";
  }
  .fa-mars-stroke:before {
    content: "\f229";
  }
  .fa-mars-stroke-v:before {
    content: "\f22a";
  }
  .fa-mars-stroke-h:before {
    content: "\f22b";
  }
  .fa-neuter:before {
    content: "\f22c";
  }
  .fa-genderless:before {
    content: "\f22d";
  }
  .fa-facebook-official:before {
    content: "\f230";
  }
  .fa-pinterest-p:before {
    content: "\f231";
  }
  .fa-whatsapp:before {
    content: "\f232";
  }
  .fa-server:before {
    content: "\f233";
  }
  .fa-user-plus:before {
    content: "\f234";
  }
  .fa-user-times:before {
    content: "\f235";
  }
  .fa-hotel:before,
  .fa-bed:before {
    content: "\f236";
  }
  .fa-viacoin:before {
    content: "\f237";
  }
  .fa-train:before {
    content: "\f238";
  }
  .fa-subway:before {
    content: "\f239";
  }
  .fa-medium:before {
    content: "\f23a";
  }
  .fa-yc:before,
  .fa-y-combinator:before {
    content: "\f23b";
  }
  .fa-optin-monster:before {
    content: "\f23c";
  }
  .fa-opencart:before {
    content: "\f23d";
  }
  .fa-expeditedssl:before {
    content: "\f23e";
  }
  .fa-battery-4:before,
  .fa-battery-full:before {
    content: "\f240";
  }
  .fa-battery-3:before,
  .fa-battery-three-quarters:before {
    content: "\f241";
  }
  .fa-battery-2:before,
  .fa-battery-half:before {
    content: "\f242";
  }
  .fa-battery-1:before,
  .fa-battery-quarter:before {
    content: "\f243";
  }
  .fa-battery-0:before,
  .fa-battery-empty:before {
    content: "\f244";
  }
  .fa-mouse-pointer:before {
    content: "\f245";
  }
  .fa-i-cursor:before {
    content: "\f246";
  }
  .fa-object-group:before {
    content: "\f247";
  }
  .fa-object-ungroup:before {
    content: "\f248";
  }
  .fa-sticky-note:before {
    content: "\f249";
  }
  .fa-sticky-note-o:before {
    content: "\f24a";
  }
  .fa-cc-jcb:before {
    content: "\f24b";
  }
  .fa-cc-diners-club:before {
    content: "\f24c";
  }
  .fa-clone:before {
    content: "\f24d";
  }
  .fa-balance-scale:before {
    content: "\f24e";
  }
  .fa-hourglass-o:before {
    content: "\f250";
  }
  .fa-hourglass-1:before,
  .fa-hourglass-start:before {
    content: "\f251";
  }
  .fa-hourglass-2:before,
  .fa-hourglass-half:before {
    content: "\f252";
  }
  .fa-hourglass-3:before,
  .fa-hourglass-end:before {
    content: "\f253";
  }
  .fa-hourglass:before {
    content: "\f254";
  }
  .fa-hand-grab-o:before,
  .fa-hand-rock-o:before {
    content: "\f255";
  }
  .fa-hand-stop-o:before,
  .fa-hand-paper-o:before {
    content: "\f256";
  }
  .fa-hand-scissors-o:before {
    content: "\f257";
  }
  .fa-hand-lizard-o:before {
    content: "\f258";
  }
  .fa-hand-spock-o:before {
    content: "\f259";
  }
  .fa-hand-pointer-o:before {
    content: "\f25a";
  }
  .fa-hand-peace-o:before {
    content: "\f25b";
  }
  .fa-trademark:before {
    content: "\f25c";
  }
  .fa-registered:before {
    content: "\f25d";
  }
  .fa-creative-commons:before {
    content: "\f25e";
  }
  .fa-gg:before {
    content: "\f260";
  }
  .fa-gg-circle:before {
    content: "\f261";
  }
  .fa-tripadvisor:before {
    content: "\f262";
  }
  .fa-odnoklassniki:before {
    content: "\f263";
  }
  .fa-odnoklassniki-square:before {
    content: "\f264";
  }
  .fa-get-pocket:before {
    content: "\f265";
  }
  .fa-wikipedia-w:before {
    content: "\f266";
  }
  .fa-safari:before {
    content: "\f267";
  }
  .fa-chrome:before {
    content: "\f268";
  }
  .fa-firefox:before {
    content: "\f269";
  }
  .fa-opera:before {
    content: "\f26a";
  }
  .fa-internet-explorer:before {
    content: "\f26b";
  }
  .fa-tv:before,
  .fa-television:before {
    content: "\f26c";
  }
  .fa-contao:before {
    content: "\f26d";
  }
  .fa-500px:before {
    content: "\f26e";
  }
  .fa-amazon:before {
    content: "\f270";
  }
  .fa-calendar-plus-o:before {
    content: "\f271";
  }
  .fa-calendar-minus-o:before {
    content: "\f272";
  }
  .fa-calendar-times-o:before {
    content: "\f273";
  }
  .fa-calendar-check-o:before {
    content: "\f274";
  }
  .fa-industry:before {
    content: "\f275";
  }
  .fa-map-pin:before {
    content: "\f276";
  }
  .fa-map-signs:before {
    content: "\f277";
  }
  .fa-map-o:before {
    content: "\f278";
  }
  .fa-map:before {
    content: "\f279";
  }
  .fa-commenting:before {
    content: "\f27a";
  }
  .fa-commenting-o:before {
    content: "\f27b";
  }
  .fa-houzz:before {
    content: "\f27c";
  }
  .fa-vimeo:before {
    content: "\f27d";
  }
  .fa-black-tie:before {
    content: "\f27e";
  }
  .fa-fonticons:before {
    content: "\f280";
  }
  .fa-reddit-alien:before {
    content: "\f281";
  }
  .fa-edge:before {
    content: "\f282";
  }
  .fa-credit-card-alt:before {
    content: "\f283";
  }
  .fa-codiepie:before {
    content: "\f284";
  }
  .fa-modx:before {
    content: "\f285";
  }
  .fa-fort-awesome:before {
    content: "\f286";
  }
  .fa-usb:before {
    content: "\f287";
  }
  .fa-product-hunt:before {
    content: "\f288";
  }
  .fa-mixcloud:before {
    content: "\f289";
  }
  .fa-scribd:before {
    content: "\f28a";
  }
  .fa-pause-circle:before {
    content: "\f28b";
  }
  .fa-pause-circle-o:before {
    content: "\f28c";
  }
  .fa-stop-circle:before {
    content: "\f28d";
  }
  .fa-stop-circle-o:before {
    content: "\f28e";
  }
  .fa-shopping-bag:before {
    content: "\f290";
  }
  .fa-shopping-basket:before {
    content: "\f291";
  }
  .fa-hashtag:before {
    content: "\f292";
  }
  .fa-bluetooth:before {
    content: "\f293";
  }
  .fa-bluetooth-b:before {
    content: "\f294";
  }
  .fa-percent:before {
    content: "\f295";
  }
  /* Style the submit button with a specific background color etc */
  button[type=submit] {
    background-color: #04AA6D;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  /* When moving the mouse over the submit button, add a darker green color */
  button[type=submit]:hover {
    background-color: #45a049;
  }
  /* Hide Streamlit Branding */
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  header {visibility: hidden;}
    </style>
    </head>
     <input type="text" name="name" placeholder="Your name"required>
     <input type="email" name="email" placeholder="Your email" required>
     <html>
<h1><b><i>SHIPMENT DETAILS</i></b></h1>
<body>
  <div class="container">
    <h2>Select Container Load</h2>
    <form>
      <label class="radio-inline">
        <input type="radio" name="Select Container Load" >FCL
      </label>
      <label class="radio-inline">
        <input type="radio" name="Select Container Load" checked>LCL
      </label>
    </form>
  </div>
  </body>
  <body>
    <label for="Choose Your INCOTERMS"><h2>Choose Your INCOTERMS</h2></label>
    <select name="Choose Your INCOTERMS" id="Choose Your INCOTERMS" required>
      <option value="Ex Works">Ex Works(EXW)</option>
      <option value="Free Carrier">Free Carrier(FCA)</option>
      <option value="Delivered Duty Paid">Delivered Duty Paid(DDP)</option>
      <option value="Cost,Insurance,Freight">Cost,Insurance,Freight(CIF)</option>
    </select>
  </body>
<div>
  <body>
    <h2>Select Your COMMODITY</h2>
    <form action="/action_page.php">
      <input list="commodities" name="browser">
      <datalist id="commodities" required>
            <option value="ALUMINIUM">
            <option value="ANIMAL FAT">
            <option value="ANIMAL FODDER">
            <option value="AGRICULTURAL PRODUCE">
            <option value="ANIMAL PRODUCTS">
            <option value="ARMS">
            <option value="ARTIFICIAL FLOWERS">
            <option value="ARTIFICIAL WAX">
            <option value="ASBESTOS">
            <option value="ASH">
            <option value="AUTO - MOTOR VEHICLES">
            <option value="AUTO PARTS">
            <option value="BEDDING">
            <option value="BEVERAGE">
            <option value="BOATS">
            <option value="CABLES">
            <option value="CANDLES">
            <option value="CARPETS">
            <option value="CEMENT">
            <option value="CERAMICS">
            <option value="CEREAL">
            <option value="CHARCOAL">
            <option value="CHEMICALS">
            <option value="CLOCKS">
            <option value="CLOTHING">
            <option value="COCOA">
            <option value="COCONUT">
            <option value="COFFEE">
            <option value="COPPER">
            <option value="COSMETICS">
            <option value="COTTON">
            <option value="CROCHETED FABRICS">
            <option value="CRUSTACEANS">
            <option value="CUSHIONS">
            <option value="CUTLERY">
            <option value="DAIRY PRODUCE">
            <option value="DEFENCE - MILITARY EQUIPMENT">
            <option value="DENTAL WAX">
            <option value="DYES">
            <option value="ELECTRICAL EQUIPMENT">
            <option value="ELECTRICAL MACHINERY">
            <option value="EMBROIDERY">
            <option value="ESSENTIAL OILS">
            <option value="EXPLOSIVES">
            <option value="FABRIC">
            <option value="FOOD GRAINS">
            <option value="FELT">
            <option value="FERTILISERS">
            <option value="FISH">
            <option value="FLOUR">
            <option value="FOOTWEAR">
            <option value="FORKS">
            <option value="FRUIT">
            <option value="FURNITURE">
            <option value="FURSKINS">
            <option value="GAMES">
            <option value="GLASS">
            <option value="GLUE">
            <option value="HAIR">
            <option value="HANDBAGS">
            <option value="HAZARDOUS GOODS">
            <option value="HEADGEAR">
            <option value="IRON">
            <option value="KNITTED FABRICS">
            <option value="LACE">
            <option value="LAMPS">
            <option value="LEAD">
            <option value="LEATHER">
            <option value="LIGHTING FITTINGS">
            <option value="LIME">
            <option value="LIVE ANIMALS">
            <option value="LUMBER">
            <option value="LUBRICANT">
            <option value="MACHINERY">
            <option value="MALT">
            <option value="MATTRESSES">
            <option value="MEAT">
            <option value="MECHANICAL APPLIANCES">
            <option value="MECHANICAL EQUIPMENT">
            <option value="MEDICAL INSTRUMENTS">
            <option value="MINERAL FUEL">
            <option value="MILK">
            <option value="MINERAL OILS">
            <option value="MINERAL WAX">
            <option value="MINERALS">
            <option value="MUSICAL INSTRUMENTS">
            <option value="NEWSPAPERS">
            <option value="NICKEL">
            <option value="NUCLEAR REACTOR">
            <option value="NUTS">
            <option value="orange">
            <option value="ORE">
            <option value="ORGANIC CHEMICALS">
            <option value="ORGANIC MANURE">
            <option value="OTHER">
            <option value="PAINT">
            <option value="PAPER">
            <option value="PERFUME">
            <option value="PERISHABLE GOODS">
            <option value="PHOTOGRAPHY GOODS">
            <option value="PLANTS">
            <option value="PLASTER">
            <option value="PLASTICS">
            <option value="POLISH">
            <option value="PRECIOUS METALS">
            <option value="PRECIOUS STONES">
            <option value="PULP">
            <option value="PULSES">
            <option value="PREPARED WAX">
            <option value="RAILWAY FIXTURES">
            <option value="RELIEF MATERIALS (For Disasters)">
            <option value="RAW HIDES">
            <option value="RAW SKINS">
            <option value="RESIN">
            <option value="RICE">
            <option value="RIDING-CROPS">
            <option value="ROPE">
            <option value="RUBBER">
            <option value="SADDLES">
            <option value="SALT">
            <option value="SEEDS">
            <option value="SHIPS">
            <option value="SILK">
            <option value="SLAG">
            <option value="SOAP">
            <option value="SOUND RECORDERS">
            <option value="SPACECRAFT">
            <option value="SPICES">
            <option value="SPIRITS">
            <option value="SPOONS">
            <option value="STARCHES">
            <option value="STEEL">
            <option value="STEEL PRODUCTS">
            <option value="STONE">
            <option value="STRAW">
            <option value="STUFFED FURNISHINGS">
      </datalist>
    </form>
    </body>
</div>
<h2>Select Pickup ORIGIN</h2>
    <datalist id="suggestions" required>
<option>Aachen,Germany</option>   
<option>Aalesund,Denmark</option>
<option>Aarhus,Denmark</option>
<option>Abaco,Bahamas</option>
<option>Abakan,Russia</option>
<option>Abidjan,Ivory Coast</option>
<option>Abu Dhabi,United Arab Emirates</option>
<option>Aburatsu,Japan</option>
<option>Acajutla,Republic of El Salvador</option>
<option>Acapulco,Mexico</option>
<option>Adabiya,Egypt</option>
<option>Addis Ababa,Ethiopia</option>
<option>Adelaide,South Australia</option>
<option>Aden,Yemen</option>
<option>Agadir,Morocco</option>
<option>Agira (Inland Point),Italy</option>
<option>Ahmedabad,India</option>
<option>Ain Sokhna,Egypt</option>
<option>Aitutaki,Cook Islands</option>
<option>Ajman,United Arab Emirates</option>
<option>Akita,Japan</option>
<option>Akmola,Kazakhstan</option>
<option>Aktau,Kazakhstan</option>
<option>Aktobe,Kazakhstan</option>
<option>Al Aqabah,Jordan</option>
<option>AL Iskandariyah,Egypt</option>
<option>AL Jubail,Saudi Arabia</option>
<option>Al Khoms,Libya</option>
<option>Alacahoyuk,Turkey</option>
<option>Alashankou,Mongolia</option>
<option>Alaska,United States</option>
<option>Albany,United States</option>
<option>Alexandria,Egypt</option>
<option>Algeciras,Spain</option>
<option>Algiers,Algeria</option>
<option>Aliaga,Turkey</option>
<option>Alicante,Spain</option>
<option>Almaty,Kazakhstan</option>
<option>Alotau,Papua New Guinea</option>
<option>Alsancak,Turkey</option>
<option>Altamira,Mexico</option>
<option>Ambarli,Turkey</option>
<option>Amman,Jordan</option>
<option>Amsterdam,Netherlands</option>
<option>An Ping,Guangdong Province</option>
<option>Anacortes,Washington</option>
<option>Anchorage,Alaska</option>
<option>Ancona,Italy</option>
<option>Anderson,South Carolina</option>
<option>Angamos,Chile</option>
<option>Annaba,Algeria</option>
<option>Anqing,Anhui Province</option>
<option>Anshun,Guizhou Province</option>
<option>Antalya,Turkey</option>
<option>Antigua,Guatemala</option>
<option>Antofagasta,Chile</option>
<option>Antwerp,Belgium</option>
<option>Anzherskaya,Russia</option>
<option>Aotou,Guangdong Province</option>
<option>Apapa,Nigeria</option>
<option>Apia,Western Samoa</option>
<option>Aqaba,Jordan</option>
<option>Aqaba Zerka Free Zone,Jordan</option>
<option>Archangelsk,Russia</option>
<option>Arica,Chile</option>
<option>Arieki,Malaysia</option>
<option>Aruba,Netherlands Antilles</option>
<option>Ashdod,Israel</option>
<option>Ashgabat,Turkmenistan</option>
<option>Ashkelon,Israel</option>
<option>Ashkhabad,Russia</option>
<option>Asmara,Ethiopia</option>
<option>Assab,Ethiopia</option>
<option>Astana,Kazakhstan</option>
<option>Astrakhan,Russia</option>
<option>Asuncion,Paraguay</option>
<option>Athens,Greece</option>
<option>Atlanta,Georgia</option>
<option>Atlixco,Mexico</option>
<option>Atyrau,Kazakhstan</option>
<option>Auckland,New Zealand</option>
<option>Auxerre,France</option>
<option>Avcilar,Turkey</option>
<option>Avignon,France</option>
<option>Azov,Russia</option>
<option>Baghdad,Iraq</option>
<option>Baguio,Philippines</option>
<option>Bahama,Caribbean</option>
<option>Bahrain,Persian Gulf</option>
<option>Baku,Azerbaijan</option>
<option>Balboa,Panama</option>
<option>Balclutha,New Zealand</option>
<option>Balikpapan,Indonesia</option>
<option>Baltimore,Maryland</option>
<option>Bamako,Mali</option>
<option>Bangalore,India</option>
<option>Bangbu,Anhui Province</option>
<option>Bangkok,Thailand</option>
<option>Bangkok (BMT),Thailand</option>
<option>Bangkok (PAT),Thailand</option>
<option>Bangkok (SCT),Thailand</option>
<option>Bangkok (TPT),Thailand</option>
<option>Bangkok (Unithai),Thailand</option>
<option>Bangkok (UTCT),Thailand</option>
<option>Bangpakong,Thailand</option>
<option>Banjul,Gambia</option>
<option>Baoan,Guangdong Province</option>
<option>Baoying,Jiangsu Province</option>
<option>Bar,Serbia</option>
<option>Barcelona,Spain</option>
<option>Bari,Italy</option>
<option>Barnaul,Russia</option>
<option>Barranquilla,Colombia</option>
<option>Bartlett,United States</option>
<option>Basamuk,Papua New Guinea</option>
<option>Basel,Switzerland</option>
<option>Basra,Iraq</option>
<option>Basse-Terre,ST. Kitts</option>
<option>Basuo,Hainan Province</option>
<option>Bata,Equatorial Guinea</option>
<option>Batam,Indonesia</option>
<option>Batangas,Philippines</option>
<option>Baton Rouge,Louisiana</option>
<option>Batu Ampar,Indonesia</option>
<option>Batumi,Georgia</option>
<option>Beaumont,U.K.</option>
<option>Beicun,Guangdong Province</option>
<option>Beihai,Guangxi Province</option>
<option>Beijiao,Guangdong Province</option>
<option>Beijing,China</option>
<option>Beira,Mozambique</option>
<option>Beirut,Lebanon</option>
<option>Bejaia,Algeria</option>
<option>Belawan,Indonesia</option>
<option>Belem,Brazil</option>
<option>Belfast,Ireland</option>
<option>Belgorad,Russia</option>
<option>Belgrade,Serbia</option>
<option>Belize,Belize</option>
<option>Bell Bay,Australia</option>
<option>Benete Bay,Indonesia</option>
<option>Benghazi,Libya</option>
<option>Benguela,Angola</option>
<option>Beograd,Serbia</option>
<option>Berbera,Somalia</option>
<option>Berkakit,Russia</option>
<option>Berlin,Germany</option>
<option>Besancon,France</option>
<option>Bielefeld,Germany</option>
<option>Bilbao,Spain</option>
<option>Bingazi,Libya</option>
<option>Bintulu,Malaysia</option>
<option>Birmingham,U.K.</option>
<option>Birobidzhan,Russia</option>
<option>Bishkek,Kyrgyzstan</option>
<option>Bissau,Guinea</option>
<option>Biysk,Russia</option>
<option>Bizerte,Tunisia</option>
<option>Blagoveschensk,Russia</option>
<option>Blantyre,Malawi</option>
<option>Blois,France</option>
<option>Bluff,New Zealand</option>
<option>Bobruysk,Russia</option>
<option>Bogota,Colombia</option>
<option>Bologna (Inland Point),Italy</option>
<option>Boma,Zaire</option>
<option>Bombay,India</option>
<option>Bonaire,Netherlands</option>
<option>Bonneuil Sur Marne,France</option>
<option>Bordeaux,France</option>
<option>Bosperus,Turkey</option>
<option>Boston,Massachusetts</option>
<option>Botswana,Africa</option>
<option>Bourg,France</option>
<option>Bratislava,Slovakia</option>
<option>Bregenz,Austria</option>
<option>Breinigsvolle,United States</option>
<option>Bremen,Germany</option>
<option>Bremerhaven,Germany</option>
<option>Briansk,Russia</option>
<option>Bridgetown,Barbados</option>
<option>Brisbane,Australia</option>
<option>Bristol,U.K.</option>
<option>Brno,Czech Republic</option>
<option>Brunei,Brunei</option>
<option>Brunswick,Georgia</option>
<option>Brussels,Belgium</option>
<option>Brzeg Dolny,Poland</option>
<option>Brzesc,Russia</option>
<option>Bucharest,Romania</option>
<option>Budapest,Hungary</option>
<option>Buenaventura,Colombia</option>
<option>Buenos Aires,Argentina</option>
<option>Bufalo,Honduras</option>
<option>Bugo,Philippines</option>
<option>Bujumbuba,East Africa</option>
<option>Bukavu,East Africa</option>
<option>Bukhara,Russia</option>
<option>Bulawayo,Zimbabwe</option>
<option>Burgas,Bulgaria</option>
<option>Burlington,New Jersey</option>
<option>Burnie,Australia</option>
<option>Busan,South Korea</option>
<option>Busan/Pui,South Korea</option>
<option>Bydgoszcz,Poland</option>
<option>Caacupemi,Paraguay</option>
<option>Cabedello,Brazil</option>
<option>Cabinda,Angola</option>
<option>Cadiz,Spain</option>
<option>Cagayan de Oro,Philippines</option>
<option>Cagliari,Italy</option>
<option>Cai Mep,Vietnam</option>
<option>Cailan,Vietnam</option>
<option>Cairns,Queensland</option>
<option>Cairo,Egypt</option>
<option>Calabar,Nigeria</option>
<option>Calcutta,India</option>
<option>Caldera,Costa Rica</option>
<option>Calgary,Alberta</option>
<option>Callao,Peru</option>
<option>Cambodia,Vietnam</option>
<option>Cambridge,New Zealand</option>
<option>Camden,U.K.</option>
<option>Can Tho,Vietnam</option>
<option>Canakkale,Turkey</option>
<option>Canoas,Brazil</option>
<option>Cantho,Vietnam</option>
<option>Cao Fei Dian,Hebei Province</option>
<option>Cape Town,South Africa</option>
<option>Cape Verde,Africa</option>
<option>Caracas,Venezuela</option>
<option>Caribbean Islands,Caribbean</option>
<option>Carson,United States</option>
<option>Cartagena,Colombia</option>
<option>Cartago,Colombia</option>
<option>Casablanca,Morocco</option>
<option>Castellon,Spain</option>
<option>Castries,ST. Lucia</option>
<option>Catania,Italy</option>
<option>Caucedo,Dominican Republic</option>
<option>Cavaglia (Inland Point),Italy</option>
<option>Cayenne Fr.,Guyana</option>
<option>Cebu,Philippines</option>
<option>Ceuta,Morocco</option>
<option>Chalon-Sur-Marne,France</option>
<option>Chalon-Sur-Saone,France</option>
<option>Chanaral,Chile</option>
<option>Changchun,Jilin Province</option>
<option>Changle,Fujian Province</option>
<option>Changsha,Hunan Province</option>
<option>Changshu,Jiangsu Province</option>
<option>Changzhou,Jiangsu Province</option>
<option>Chaohu,Anhui Province</option>
<option>Chaozhou,Guangdong Province</option>
<option>Charkov,Russia</option>
<option>Charleston,South Carolina</option>
<option>Charlestown,Nevis</option>
<option>Charlotte,North Carolina</option>
<option>Charlotte Amalie,ST. Thomas</option>
<option>Chattanooga,Tennessee</option>
<option>Chattogram,Bangladesh</option>
<option>Cheljabinsk,Russia</option>
<option>Chen Lian Ji,Hunan Province</option>
<option>Chengdu,Sichuan Province</option>
<option>Chenghai,Guangdong Province</option>
<option>Chenglingji,Hunan Province</option>
<option>Chennai,India</option>
<option>Cherkassy,Ukraine</option>
<option>Chiasso,Switzerland</option>
<option>Chiba,Japan</option>
<option>Chicago,Illinois</option>
<option>Chimbote,Chile</option>
<option>Chimkent,Kazakhstan</option>
<option>Chingyuan,Henan Province</option>
<option>Chistiansted,ST. Croix</option>
<option>Chita,Russia</option>
<option>Chittagong,Bangladesh</option>
<option>Chiwan,Guangdong Province</option>
<option>Choloma,Honduras</option>
<option>Chongqing,China</option>
<option>Christchurch,New Zealand</option>
<option>Christiansted,ST. Croix</option>
<option>Chu Lai,Vietnam</option>
<option>Chuangsha,Jiangsu Province</option>
<option>Chuansha,Shanghai</option>
<option>Chuuk,Micronesia Islands</option>
<option>Chymkent,Kyrgyzstan</option>
<option>Cincinnati,Ohio</option>
<option>Ciudad Del Este,Paraguay</option>
<option>Civitavecchia,Italy</option>
<option>Clermont-Ferrand,France</option>
<option>Cleveland,Ohio</option>
<option>Coatzacoalcos,Mexico</option>
<option>Cochabamba,Bolivia</option>
<option>Cochin,India</option>
<option>Cocosolo,Panama</option>
<option>Coega-Ngqura,South Africa</option>
<option>Coimbatore,India</option>
<option>Cologne,Germany</option>
<option>Cologno Monzese (Inland Point),Italy</option>
<option>Colombo,Sri Lanka</option>
<option>Colon,Panama</option>
<option>Columbus,Ohio</option>
<option>Comores,India</option>
<option>Conakry,Guinea</option>
<option>Conception Bay,Chile</option>
<option>Connellsville,United States</option>
<option>Constanta,Romania</option>
<option>Copenhagen,Denmark</option>
<option>Coquimbo,Chile</option>
<option>Cordoba,Argentina</option>
<option>Corinto,Nicaragua</option>
<option>Cork,Ireland</option>
<option>Coronel,Chile</option>
<option>Corpus Christi,United States</option>
<option>Corsicana,Texas</option>
<option>Cotabato,Philippines</option>
<option>Cotonou,Benin</option>
<option>Cremona (Inland Point),Italy</option>
<option>Cristobal,Panama</option>
<option>Cuemavaca,Mexico</option>
<option>Cuenca,Spain</option>
<option>Curacao,Curacao</option>
<option>Curitiba,Brazil</option>
<option>Czestochowa,Poland</option>
<option>Da Chan Bay,Guangdong Province</option>
<option>Dachen,Zhejiang Province</option>
<option>Dadri,India</option>
<option>Daesan,South Korea</option>
<option>Dafeng,Jiangsu Province</option>
<option>Daganwei (Guangzhou),Guangdong Province</option>
<option>Dakar,Senegal</option>
<option>Dalian,Liaoning Province</option>
<option>Dallas,Texas</option>
<option>Dalta Port,Egypt</option>
<option>Damietta,Egypt</option>
<option>Dammam,Saudi Arabia</option>
<option>Dampier,Australia</option>
<option>Danang,Vietnam</option>
<option>Dandong,Liaoning Province</option>
<option>Dapeng,Guangdong Province</option>
<option>Dar es Salaam,Tanzania</option>
<option>Darkhan,Mongolia</option>
<option>Darwin,Australia</option>
<option>Datian,Fujian Province</option>
<option>Datong,Guangdong Province</option>
<option>Davao,Philippines</option>
<option>Dayabay,Guangdong Province</option>
<option>Dekheila,Egypt</option>
<option>Delhi,India</option>
<option>Denver,Colorado</option>
<option>Derince,Turkey</option>
<option>Derna,Libya</option>
<option>Destrehan,United States</option>
<option>Detroit,Michigan</option>
<option>Dhaka,Bangladesh</option>
<option>Diego Suarez,Madagascar</option>
<option>Dijon,France</option>
<option>Dili,Timor</option>
<option>Djen Djen,Algeria</option>
<option>Djibouti,East Africa</option>
<option>Dnepropetrovsk,Russia</option>
<option>Do Ma Tou,Guangdong Province</option>
<option>Doha,Qatar</option>
<option>Dole,France</option>
<option>Dominican,Dominican Republic</option>
<option>Donetsk,Ukraine</option>
<option>Dongguan,Guangdong Province</option>
<option>Dongjiakou,Guangdong Province</option>
<option>Dongjiangcang,Guangdong Province</option>
<option>Dongshan,Fujian Province</option>
<option>Dortmund,Germany</option>
<option>Douala,Cameroon</option>
<option>Doumen,Guangdong Province</option>
<option>Dresden,Germany</option>
<option>Druzba,Kazakhstan</option>
<option>Dubai,United Arab Emirates</option>
<option>Dublin,Ireland</option>
<option>Duesseldorf,Germany</option>
<option>Duisburg,Germany</option>
<option>Dumyat,Egypt</option>
<option>Dunedin,New Zealand</option>
<option>Dunkerque,France</option>
<option>Dunkirk,France</option>
<option>Durban,South Africa</option>
<option>Durres,Albania</option>
<option>Dushanbe,Tajikistan</option>
<option>Dusseldorf,Germany</option>
<option>Dutch Harbor,United States</option>
<option>Dzaoudzi,Mayotte</option>
<option>Dzhezkazgan,Kazakhstan</option>
<option>East Canada,Canada</option>
<option>East London,South Africa</option>
<option>Ebeye,Marina Islands</option>
<option>Edincik,Turkey</option>
<option>Edison,New Jersey</option>
<option>Edmonton,Canada</option>
<option>Ehoala,Madagascar</option>
<option>Eilat,Israel</option>
<option>Ekaterinburg,Russia</option>
<option>El Dekhelia,Egypt</option>
<option>El Guamache,Venezuela</option>
<option>El Paso,Honduras</option>
<option>El Progreso,Honduras</option>
<option>El Salvador,Republic of El Salvador</option>
<option>El-Dekheila,Egypt</option>
<option>Embakasi,Kenya</option>
<option>Encarnacion,Mexico</option>
<option>Enping,Guangdong Province</option>
<option>Ensenada,Mexico</option>
<option>Erdenet,Mongolia</option>
<option>Eren,Inner Mongolia</option>
<option>Erlian,Inner Mongolia</option>
<option>Esmeraldas,Ecuador</option>
<option>Esperance,Australia</option>
<option>Essen,Germany</option>
<option>Estonia,Russia</option>
<option>Everett,Washington</option>
<option>Evyap Port,Turkey</option>
<option>Exuma,Bahamas</option>
<option>Famagusta,Cyprus</option>
<option>Fangcheng,Guangxi Province</option>
<option>Fangcun,Guangdong Province</option>
<option>Felixstowe,U.K.</option>
<option>Fenghua,Zhejiang Province</option>
<option>Fenghuojiao (Tai Shan),Guangdong Province</option>
<option>Fengxian,Jiangsu Province</option>
<option>Fergana,Russia</option>
<option>Fernandina Beach,Florida</option>
<option>Florence,Italy</option>
<option>Floroe,Norway</option>
<option>Flushing,Netherlands</option>
<option>Fontana,California</option>
<option>Fort de France,Martinique</option>
<option>Fortaleza,Brazil</option>
<option>Fos Sur Mer,France</option>
<option>Foshan,Guangdong Province</option>
<option>Frankfurt,Germany</option>
<option>Fredericia,Denmark</option>
<option>Freeport,Bahamas</option>
<option>Freetown,Sierra Leone</option>
<option>Fremantle,Western Australia</option>
<option>Fremont,California</option>
<option>Frontroyal,Virginia</option>
<option>Frunze,Russia</option>
<option>Fujairah,United Arab Emirates</option>
<option>Fukuoka,Japan</option>
<option>Fukuyama,Japan</option>
<option>Funafuti,Tuvalu</option>
<option>Fuqing,Fujian Province</option>
<option>Fuzhou,Fujian Province</option>
<option>Gaborone,Botswana</option>
<option>Galveston,Texas</option>
<option>Gamagori,Japan</option>
<option>Gaolan (Zhuhai),Guangdong Province</option>
<option>Gaoming,Guangdong Province</option>
<option>Gaosha,Guangdong Province</option>
<option>Gaoyao,Guangdong Province</option>
<option>Gaoyou,Jiangsu Province</option>
<option>Gatemala City,Guatemala</option>
<option>Gatun,Panama</option>
<option>Gdansk,Poland</option>
<option>Gdynia,Poland</option>
<option>Gebze,Turkey</option>
<option>Geelong,Australia</option>
<option>Gemlik,Turkey</option>
<option>General Santos City,Philippines</option>
<option>Geneve,Switzerland</option>
<option>Gennevilliers,France</option>
<option>Genoa (Genova),Italy</option>
<option>Geoje,South Korea</option>
<option>George Town,Guyana</option>
<option>Geraldton,Australia</option>
<option>Ghazaouete,Algeria</option>
<option>Ghent,Belgium</option>
<option>Gibraltar,Spain</option>
<option>Gijon,Spain</option>
<option>Gioia Tauro,Italy</option>
<option>Girdwood,Alaska</option>
<option>Gladstone,Australia</option>
<option>Glasgow,Scotland</option>
<option>Gliwice,Poland</option>
<option>Gomel,Russia</option>
<option>Gongyi,Henan Province</option>
<option>Gothenburg,Sweden</option>
<option>Grand Rapids,United States</option>
<option>Grand Turk,Caribbean</option>
<option>Grangemouth,U.K.</option>
<option>Grays,U.K.</option>
<option>Graz,Austria</option>
<option>Greensboro,North Carolina</option>
<option>Guadalajara,Mexico</option>
<option>Guam,Mariana Islands</option>
<option>Guang Bao Tong,Guangdong Province</option>
<option>Guangzhou,Guangdong Province</option>
<option>Guanta,Venezuela</option>
<option>Guarulhos,Brazil</option>
<option>Guatemala City,Guatemala</option>
<option>Guayaquil,Ecuador</option>
<option>Guaymas,Mexico</option>
<option>Guigang,Guangxi Province</option>
<option>Guilin,Guangxi Province</option>
<option>Guinea-Bissau,Western Africa</option>
<option>Guiyang,Guizhou Province</option>
<option>Guizhou,Guangdong Province</option>
<option>Gustavia,ST. Barths</option>
<option>Gwangyang,South Korea</option>
<option>Hachinohe,Japan</option>
<option>Hagen,Germany</option>
<option>Haian,Hainan Province</option>
<option>Haifa,Israel</option>
<option>Haifeng,Guangdong Province</option>
<option>Haikou,Hainan Province</option>
<option>Haimen,Zhejiang Province</option>
<option>Hainan,Fujian Province</option>
<option>Haining,Zhejiang Province</option>
<option>Haiphong,Vietnam</option>
<option>Hairaton,Afghanistan</option>
<option>Hairun,Fujian Province</option>
<option>Haiti,Caribbean</option>
<option>Haitian,Fujian Province</option>
<option>Hakata,Japan</option>
<option>Hakodate,Japan</option>
<option>Haldia,India</option>
<option>Halifax,Nova Scotia</option>
<option>Hamad Port,Qatar</option>
<option>Hamada,Japan</option>
<option>Hamburg,Germany</option>
<option>Hamilton,New Zealand</option>
<option>Hamina,Finland</option>
<option>Hangzhou,Zhejiang Province</option>
<option>Hanjiang,Fujian Province</option>
<option>Hankou,Hubei Province</option>
<option>Hannover,Germany</option>
<option>Hanoi,Vietnam</option>
<option>Harare,Zimbabwe</option>
<option>Harbin,Heilongjiang Province</option>
<option>Hartford,Michigan</option>
<option>Haydarpasa,Turkey</option>
<option>Hazira,India</option>
<option>Hebron,Ohio</option>
<option>Hefei,Anhui Province</option>
<option>Hehou (Xin Hui),Guangdong Province</option>
<option>Helsingborg,Sweden</option>
<option>Helsinki,Finland</option>
<option>Hengyang,Hunan Province</option>
<option>Herakleion,Greece</option>
<option>Heshan,Guangdong Province</option>
<option>Hialeah,United States</option>
<option>Hibiki,Japan</option>
<option>Hibikinada,Japan</option>
<option>Higashiharima,Japan</option>
<option>Hilo,Hawaii</option>
<option>Himeji,Japan</option>
<option>Hiroshima,Japan</option>
<option>Hitachi,Japan</option>
<option>Hitachinaka,Japan</option>
<option>Ho Chi Minh (Catlai),Vietnam</option>
<option>Ho Chi Minh (Newport),Vietnam</option>
<option>Ho Chi Minh City,Vietnam</option>
<option>Hobart,Australia</option>
<option>Hodeidah,Yemen</option>
<option>Hohhot,Inner Mongolia</option>
<option>Hon Gai,Vietnam</option>
<option>Hong Kong,Hong Kong</option>
<option>Hongkou,Jiangsu Province</option>
<option>Honiara,Solomon Islands</option>
<option>Honolulu,Hawaii</option>
<option>Hososhima,Japan</option>
<option>Houston,Texas</option>
<option>Hua Sai,Vietnam</option>
<option>Huadu,Guangdong Province</option>
<option>Huainan,Anhui Province</option>
<option>Huang Dao,South Korea</option>
<option>Huang Shi,Hubei Province</option>
<option>Huanghua,Hebei Province</option>
<option>Huangpu,Guangdong Province</option>
<option>Huangqi,Fujian Province</option>
<option>Huangshan,Anhui Province</option>
<option>Huizhou,Guangdong Province</option>
<option>Hull,U.K.</option>
<option>Humen,Guangdong Province</option>
<option>Huntington,United States</option>
<option>Huntsville,United States</option>
<option>Hyderabad,India</option>
<option>Hyogo,Japan</option>
<option>Ijmuiden,Netherlands</option>
<option>Iligan,Philippines</option>
<option>Illichivsk,Ukraine</option>
<option>Ilo,Peru</option>
<option>Ilyichevsk,Ukraine</option>
<option>Imabari,Japan</option>
<option>Imari,Japan</option>
<option>Imbituba,Brazil</option>
<option>Immingham,U.K.</option>
<option>Inchon,South Korea</option>
<option>Indianapolis,Indiana</option>
<option>Innsbruck,Austria</option>
<option>Innxv,India</option>
<option>Invercargill,New Zealand</option>
<option>Invergordon,Scotland</option>
<option>Ipoh,Malaysia</option>
<option>Ipswich,U.K.</option>
<option>Iquique,Chile</option>
<option>Irbid,Jordan</option>
<option>Irkutsk,Russia</option>
<option>Irun,Spain</option>
<option>Ishigaki,Japan</option>
<option>Ishikari,Japan</option>
<option>Ishikariwan,Japan</option>
<option>Ishino Maki,Japan</option>
<option>Iskenderun,Turkey</option>
<option>Islam Qala,Afghanistan</option>
<option>Istanbul,Turkey</option>
<option>Itaguai,Brazil</option>
<option>Itajai,Brazil</option>
<option>Itapetinga,Brazil</option>
<option>Itapoa,Brazil</option>
<option>Itaqui,Brazil</option>
<option>Iwakuni,Japan</option>
<option>Iyomishima,Japan</option>
<option>Izmir,Turkey</option>
<option>Izmit,Turkey</option>
<option>Izmit Korfezi,Turkey</option>
<option>Jacksonville,Florida</option>
<option>Jaipur,India</option>
<option>Jakarta,Indonesia</option>
<option>Jakarta UTC1,Indonesia</option>
<option>Jakarta UTC3,Indonesia</option>
<option>Jawaharlal Nehru,India</option>
<option>Jebel Ali,United Arab Emirates</option>
<option>Jebel Ali Freezone,United Arab Emirates</option>
<option>Jeddah,Saudi Arabia</option>
<option>Jelenia Gora,Poland</option>
<option>Jiading,Shanghai</option>
<option>Jiamusi,Heilongjiang Province</option>
<option>Jiang Tang,China</option>
<option>Jiangmen,Guangdong Province</option>
<option>Jiangyin,Jiangsu Province</option>
<option>Jiankou,Fujian Province</option>
<option>Jiaojiang,Zhejiang Province</option>
<option>Jiaokou,Guangdong Province</option>
<option>Jiaoxin,Guangdong Province</option>
<option>Jiaxing,Zhejiang Province</option>
<option>Jiazi (Lu Feng),Guangdong Province</option>
<option>Jieyang,Guangdong Province</option>
<option>Jinan,Shandong Province</option>
<option>Jing Tang,Shandong Province</option>
<option>Jingan,Guangdong Province</option>
<option>Jinghua,Zhejiang Province</option>
<option>Jingjiang,Jiangsu Province</option>
<option>Jinguzhou,Guangdong Province</option>
<option>Jinshan,Shanghai</option>
<option>Jinzhou,Liaoning Province</option>
<option>Jisi,Guangdong Province</option>
<option>Jiujiang,Jiangxi Province</option>
<option>Jiujiang (Nanhai),Guangdong Province</option>
<option>Jiuzhou,Guangdong Province</option>
<option>Johannesburg,South Africa</option>
<option>Johor,Malaysia</option>
<option>Jubail,Saudi Arabia</option>
<option>Kabil,Indonesia</option>
<option>Kabul,Afghanistan</option>
<option>Kachkanar,Russia</option>
<option>Kaduna,Nigeria</option>
<option>Kagoshima,Japan</option>
<option>Kahului,Hawaii</option>
<option>Kaifeng,Henan Province</option>
<option>Kaiping,Guangdong Province</option>
<option>Kakinada,India</option>
<option>Kakogawa,Japan</option>
<option>Kaliningrad,Russia</option>
<option>Kaluga,Russia</option>
<option>Kam Pong Som,Cambodia</option>
<option>Kamchatka,Russia</option>
<option>Kampala,Uganda</option>
<option>Kanazawa,Japan</option>
<option>Kandahar,Afghanistan</option>
<option>Kandla,India</option>
<option>Kansas City,Kansas</option>
<option>Kantang,Thailand</option>
<option>Kaohsiung,China Taiwan</option>
<option>Karachi,Pakistan</option>
<option>Karaganda,Kazakhstan</option>
<option>Karatsu,Japan</option>
<option>Kashima,Japan</option>
<option>Kassel,Germany</option>
<option>Kathmandu,Nepal</option>
<option>Katowice,Poland</option>
<option>Kattupalli,India</option>
<option>Kavieng,Papua New Guinea</option>
<option>Kavkaz,Russia</option>
<option>Kawaihae,Hawaii</option>
<option>Kawasaki,Japan</option>
<option>Kayes,Mali</option>
<option>Kazan,Russia</option>
<option>Kearny,New Jersey</option>
<option>Keelung,China Taiwan</option>
<option>Kemaman,Malaysia</option>
<option>Kemerovo,Russia</option>
<option>Kenai,Alaska</option>
<option>Kent,United States</option>
<option>Khabarovsk,Russia</option>
<option>Khalifa,United Arab Emirates</option>
<option>Kharkov,Ukraine</option>
<option>Khartoum,Sudan</option>
<option>Khasan,Russia</option>
<option>Khoms,Africa</option>
<option>Khor Fakkan,United Arab Emirates</option>
<option>Khorol,Russia</option>
<option>Khudjand,Kazakhstan</option>
<option>Kiel,Germany</option>
<option>Kielce,Poland</option>
<option>Kiev,Ukraine</option>
<option>Kimbe,Papua New Guinea</option>
<option>Kimitsu,Japan</option>
<option>King Abdullah,Saudi Arabia</option>
<option>Kingston,Jamaica</option>
<option>Kingstown,Saint Vincent</option>
<option>Kinshasa,Zaire</option>
<option>Kishinev,Russia</option>
<option>Kismayu,Somalia</option>
<option>Klagenfurt,Austria</option>
<option>Klaipeda,Lithuania</option>
<option>Kobe,Japan</option>
<option>Kochi,Japan</option>
<option>Kokura,Japan</option>
<option>Kolkata,India</option>
<option>Koln,Germany</option>
<option>Koming,Guangdong Province</option>
<option>Kompong Som,Cambodia</option>
<option>Komsomolsk Na Amur,Russia</option>
<option>Koper,Slovenia</option>
<option>Koror,Palau</option>
<option>Korsakov,Russia</option>
<option>Koshichang,Japan</option>
<option>Kosrae,Micronesia Islands</option>
<option>Kota Kinabalu,Malaysia</option>
<option>Kotka,Finland</option>
<option>Krakow,Poland</option>
<option>Krasnodar,Russia</option>
<option>Krasnovosk,Russia</option>
<option>Krasnoyarsk,Russia</option>
<option>Kribi,Africa</option>
<option>Krishnapatnam,India</option>
<option>Kristiansand,Norway</option>
<option>Kuala Lumpur,Malaysia</option>
<option>Kuantan,Malaysia</option>
<option>Kuching,Malaysia</option>
<option>Kumamoto,Japan</option>
<option>Kumport,Turkey</option>
<option>Kunming,Yunnan Province</option>
<option>Kunsan,South Korea</option>
<option>Kunshan,Jiangsu Province</option>
<option>Kure,Japan</option>
<option>Kurgan,Russia</option>
<option>Kursk,Russia</option>
<option>KUSAN,South Korea</option>
<option>Kushiro,Japan</option>
<option>Kustany,Kazakhstan</option>
<option>Kuwait,Persian Gulf</option>
<option>Kuybyshev,Russia</option>
<option>Kwajalein,Micronesia Islands</option>
<option>Kwangyang,South Korea</option>
<option>Kyoto,Japan</option>
<option>La Ceiba,Honduras</option>
<option>La Goulette,Tunisia</option>
<option>La Guaira,Venezuela</option>
<option>La Lima,Honduras</option>
<option>La Paz,Bolivia</option>
<option>La Spezia,Italy</option>
<option>La Union,Republic of El Salvador</option>
<option>Labuan,Malaysia</option>
<option>Lae,Papua New Guinea</option>
<option>Laem Chabang,Thailand</option>
<option>Lagos/Apapa,Nigeria</option>
<option>Lahat Datu,Malaysia</option>
<option>Lahore,Pakistan</option>
<option>Laizhou,Guangdong Province</option>
<option>Lake Charles,United States</option>
<option>Lancaster,California</option>
<option>Lanshan,Henan Province</option>
<option>Lanshi,Guangdong Province</option>
<option>Lanxi,Guangdong Province</option>
<option>Lanzhou,Gansu Province</option>
<option>Laon,France</option>
<option>Laos,Thailand</option>
<option>Laredo,United States</option>
<option>Larnaca,Cyprus</option>
<option>Larvik,Norway</option>
<option>Las Minas,Guatemala</option>
<option>Las Palmas,Canary Islands</option>
<option>Lat Krabang,Thailand</option>
<option>Latvia,Russia</option>
<option>Lautoka,Fiji Island</option>
<option>Lawrence,Kansas</option>
<option>Lazaro Cardenas,Mexico</option>
<option>Le Havre,France</option>
<option>Le Verdon,France</option>
<option>Leeds,U.K.</option>
<option>Leghorn (Livorno),Italy</option>
<option>Leicester,U.K.</option>
<option>Leipzig,Germany</option>
<option>Leith,U.K.</option>
<option>Leixoes,Portugal</option>
<option>Leliu,Guangdong Province</option>
<option>Leninabad,Russia</option>
<option>Leon,Mexico</option>
<option>Lerma,Spain</option>
<option>Lerma Estado de Mexico,Mexico</option>
<option>Lesotho,Maseru</option>
<option>Levin,New Zealand</option>
<option>Lianhuashan,Guangdong Province</option>
<option>Lianyungang,Jiangsu Province</option>
<option>Liaoning,China</option>
<option>Libreville,Gabon</option>
<option>Lihir,Papua New Guinea</option>
<option>Lilongwe,Malawi</option>
<option>Lima,Peru</option>
<option>Limassol,Cyprus</option>
<option>Limon,Costa Rica</option>
<option>Linbai,Zhejiang Province</option>
<option>Linkoping,Sweden</option>
<option>Linyi,Shandong Province</option>
<option>Linz,Austria</option>
<option>Lipetsk,Russia</option>
<option>Lirquen,Chile</option>
<option>Lisbon,Portugal</option>
<option>Lithuania,Russia</option>
<option>Liudu,Guangdong Province</option>
<option>Liuzhou,Guangxi Province</option>
<option>Liverpool,U.K.</option>
<option>Livorno,Italy</option>
<option>Ljubljana,Slovenia</option>
<option>Llyichevsk,Ukraine</option>
<option>Lobito,Angola</option>
<option>Lodz,Poland</option>
<option>Lome,Togo</option>
<option>London,U.K.</option>
<option>London Gateway Port,U.K.</option>
<option>Long Beach,California</option>
<option>Long Island,Bahamas</option>
<option>Longkou,Shandong Province</option>
<option>Longoni,Africa</option>
<option>Longtan,Jiangsu Province</option>
<option>Loni,India</option>
<option>Lorengau,Papua New Guinea</option>
<option>Los Angeles,California</option>
<option>Louisville,United States</option>
<option>Luanda,Angola</option>
<option>Lubango,Angola</option>
<option>Lublin,Poland</option>
<option>Lubljana,Slovenia</option>
<option>Lubumbashi,Congo</option>
<option>Ludhiana,India</option>
<option>Ludiana,India</option>
<option>Lumut,Indonesia</option>
<option>Luoyang,Henan Province</option>
<option>Lusaka,Zambia</option>
<option>Luxembourg,Luxembourg</option>
<option>Luzhou,Sichuan Province</option>
<option>Lvov,Russia</option>
<option>Lyon,France</option>
<option>Lyttelton,New Zealand</option>
<option>Ma An Shan,Anhui Province</option>
<option>Maaloy,Norway</option>
<option>Macau,China</option>
<option>Maceio,Brazil</option>
<option>Mackay,Queensland</option>
<option>Macon,France</option>
<option>Madagascar,Africa</option>
<option>Madang,Papua New Guinea</option>
<option>Madison,N.Y.</option>
<option>Madras,India</option>
<option>Madrid,Spain</option>
<option>Maerak,Indonesia</option>
<option>Mafang,Guangdong Province</option>
<option>Magadan,Russia</option>
<option>Magnitogorsk,Russia</option>
<option>Mahajunga,Africa</option>
<option>Mahe,Seychelles</option>
<option>Mailiao,China Taiwan</option>
<option>Maizuru,Japan</option>
<option>Majunga,Madagascar</option>
<option>Majuro,Marshall Islands</option>
<option>Makasaar,Indonesia</option>
<option>Malabo,Equatorial Guinea</option>
<option>Malacca,Malaysia</option>
<option>Malaga,Canary Islands</option>
<option>Malawi,Africa</option>
<option>Male,Maldves</option>
<option>Malmo,Sweden</option>
<option>Malongo,Angola</option>
<option>Malta,Malta</option>
<option>Managua,Nicaragua</option>
<option>Manaus,Brazil</option>
<option>Manchester,U.K.</option>
<option>Mangalore,India</option>
<option>Mangyshlak,Kazakhstan</option>
<option>Manila (MICT),Philippines</option>
<option>Manila (North),Philippines</option>
<option>Manila (South),Philippines</option>
<option>Mannheim,Germany</option>
<option>Manta,Ecuador</option>
<option>Manzanillo,Mexico</option>
<option>Manzanillo (P),Panama</option>
<option>Manzhouli,Inner Mongolia</option>
<option>Maoming,Guangdong Province</option>
<option>Maptaput,Thailand</option>
<option>Maputo,Mozambique</option>
<option>Mar Del Plata,Argentina</option>
<option>Maracaibo,Venezuela</option>
<option>Mardas,Turkey</option>
<option>Margarita,Venezuela</option>
<option>Mariupol,Russia</option>
<option>Marmagao,India</option>
<option>Marport,Turkey</option>
<option>Marsa Ei Brega,Libya</option>
<option>Marsaxlokk,Malta</option>
<option>Marsdan Point,New Zealand</option>
<option>Marseilles,France</option>
<option>Marseilles-Fos,France</option>
<option>Marsh Harbour,Bahamas</option>
<option>Masan,South Korea</option>
<option>Maseru,Lesotho</option>
<option>Massawa,Ethiopia</option>
<option>Matadi,Zaire</option>
<option>Matarani,Peru</option>
<option>Matsuyama,Japan</option>
<option>Mauritius,Africa</option>
<option>Mawan,Guangdong Province</option>
<option>Mawei,Fujian Province</option>
<option>Mayotte,Comores Islands</option>
<option>Mazar-I-Sharif,Afghanistan</option>
<option>Mcdondough,United States</option>
<option>Medan,Indonesia</option>
<option>Medeu,Kazakhstan</option>
<option>Megion,Russia</option>
<option>Mejillones,Chile</option>
<option>Melbourne,Australia</option>
<option>Melilla,Morocco</option>
<option>Memphis,Tennessee</option>
<option>Mendoza,Argentina</option>
<option>Merak,Indonesia</option>
<option>Meridian,United States</option>
<option>Mersin,Turkey</option>
<option>Mexicali,Mexico</option>
<option>Mexico City,Mexico</option>
<option>Miami,Florida</option>
<option>Middlesbrough,U.K.</option>
<option>Miike,Japan</option>
<option>Milan (Inland Point),Italy</option>
<option>Milwaukee,South Dakota</option>
<option>Mina Qaboos,Persian Gulf</option>
<option>Mindanao,Philippines</option>
<option>Mindelo,Cape Varde</option>
<option>Minneapolis,Minnesota</option>
<option>Minnesota,United States</option>
<option>Minsk,Russia</option>
<option>Mira Loma,California</option>
<option>Miri,Malaysia</option>
<option>Miskolc,Hungary</option>
<option>Mississauga,Canada</option>
<option>Misurata,Libya</option>
<option>Mizushima,Japan</option>
<option>Mobile,Alabama</option>
<option>Mogadiscio,Somalia</option>
<option>Mogilev,Russia</option>
<option>Moji,Japan</option>
<option>Mokop,South Korea</option>
<option>Mombasa,Kenya</option>
<option>Mongla,Bangladesh</option>
<option>Monrovia,Liberia</option>
<option>Montego Bay,Jamaica</option>
<option>Monterrey,Mexico</option>
<option>Montevideo,Uruguay</option>
<option>Montgomery,Maryland</option>
<option>Montoir,France</option>
<option>Montpellier,France</option>
<option>Montreal,Quebec</option>
<option>Montserrat,Caribbean</option>
<option>Morehead City,North Carolina</option>
<option>Mormagao,India</option>
<option>Moroni,Comores Islands</option>
<option>Morristown,Tennessee</option>
<option>Morrisville,Pennsylvania</option>
<option>Moscow,Russia</option>
<option>Mostaganem,Algeria</option>
<option>Motukea,Papua New Guinea</option>
<option>Muara,Brunei</option>
<option>Mucuripe,Brazil</option>
<option>Mudanjiang,Heilongjiang Province</option>
<option>Mukalla,South Yemen</option>
<option>Mulund,India</option>
<option>Mumbai,India</option>
<option>Mundra,India</option>
<option>Munich,Germany</option>
<option>Muplu,Mauritius Is.</option>
<option>Murmans,Russia</option>
<option>Murmansk,Russia</option>
<option>Muroran,Japan</option>
<option>Muscat,Oman</option>
<option>Mutare,Zimbabwe</option>
<option>Mutsamudu,Comores Islands</option>
<option>Nacala,Mozambique</option>
<option>Nagasaki,Japan</option>
<option>Nagoya,Japan</option>
<option>Naha,Japan</option>
<option>Nairobi,Kenya</option>
<option>Nakanoseki,Japan</option>
<option>Nakhodka,Russia</option>
<option>Namangan,Uzbekistan</option>
<option>Namibe,Angola</option>
<option>Nanao,Guangdong Province</option>
<option>Nanchang,Jiangxi Province</option>
<option>Nangang (Nanhai),Guangdong Province</option>
<option>Nanguang,Sichuan Province</option>
<option>Nanhai,Guangdong Province</option>
<option>Nanhai (Sanshan),Guangdong Province</option>
<option>Nanhui,Shanghai</option>
<option>Nanjing,Jiangsu Province</option>
<option>Nankeng,Hunan Province</option>
<option>Nanning,Guangxi Province</option>
<option>Nansha (Guangzhou),Guangdong Province</option>
<option>Nantong,Jiangsu Province</option>
<option>Naoetsu,Japan</option>
<option>Napier,New Zealand</option>
<option>Naples,Italy</option>
<option>Narathiwat,Thailand</option>
<option>Nashville,Tennessee</option>
<option>Nassau,Bahamas</option>
<option>Nauru,Nauru</option>
<option>Navegantes,Brazil</option>
<option>Nawilwili,Hawaii</option>
<option>Ndola,Zambia</option>
<option>Nelson,New Zealand</option>
<option>Nemrut Bay,Turkey</option>
<option>Neryungri,Russia</option>
<option>Nevers,France</option>
<option>New Castle,U.K.</option>
<option>New Delhi,India</option>
<option>New Jersey,New Jersey</option>
<option>New London,United States</option>
<option>New Orleans,Louisiana</option>
<option>New Plymouth,New Zealand</option>
<option>New York,N.Y.</option>
<option>New York Harbour,N.Y.</option>
<option>Newark,New Jersey</option>
<option>Newcastle,Australia</option>
<option>Newport News,Virginia</option>
<option>Ngqura,South Africa</option>
<option>Nhatrang,Vietnam</option>
<option>Nhava Sheva,India</option>
<option>Nigqura,India</option>
<option>Niigata,Japan</option>
<option>Ningbo,Zhejiang Province</option>
<option>Ningde,Fujian Province</option>
<option>Niue,Cook Islands</option>
<option>Nizhnevartovsk,Russia</option>
<option>Nizhny Novgorod,Russia</option>
<option>Nizhny Tagil,Russia</option>
<option>Nogales,Mexico</option>
<option>Nola,Italy</option>
<option>Norfolk,Virginia</option>
<option>Noro,Solomon Islands</option>
<option>Norrkoping,Sweden</option>
<option>Northlake,United States</option>
<option>Nossi-Be,Madagascar</option>
<option>Nosy Be,Madagascar</option>
<option>Nottingham,U.K.</option>
<option>Nouadhibou,Mauritania</option>
<option>Nouakchott,Mauritania</option>
<option>Noumea,New Caledonia</option>
<option>Novgorod,Russia</option>
<option>Novokuznetsk,Mexico</option>
<option>Novorossiysk,Russia</option>
<option>Novorosyjsk,Russia</option>
<option>Novosibirsk,Russia</option>
<option>Noyabrjsk,Russia</option>
<option>Nsict,India</option>
<option>Nuernberg,Germany</option>
<option>Nuevo Laredo,Mexico</option>
<option>Nukualofa,Tonga</option>
<option>Oakland,California</option>
<option>Oamaru,New Zealand</option>
<option>Odessa,Ukraine</option>
<option>Oita,Japan</option>
<option>Okayama,Japan</option>
<option>Okinawa,Japan</option>
<option>Omaezaki,Japan</option>
<option>Omaha,Nebraska</option>
<option>Omsk,Russia</option>
<option>Onahama,Japan</option>
<option>Onne,Nigeria</option>
<option>Onsan,South Korea</option>
<option>Oporto,Portugal</option>
<option>Oran,Algeria</option>
<option>Oranjestad,Aruba</option>
<option>Orlando,Florida</option>
<option>Orleans,France</option>
<option>Orobay,Papua New Guinea</option>
<option>Orsa,Russia</option>
<option>Orzea,Russia</option>
<option>Osaka,Japan</option>
<option>Osh,Kyrgyzstan</option>
<option>Oslo,Norway</option>
<option>Otake,Japan</option>
<option>Otalu,Japan</option>
<option>Otaru,Japan</option>
<option>Oxford,U.K.</option>
<option>Padang,Indonesia</option>
<option>Pagny,France</option>
<option>Pago Pago,American Samoa</option>
<option>Paita,Peru</option>
<option>Palembang,Indonesia</option>
<option>Palermo,Italy</option>
<option>Palmerston North,New Zealand</option>
<option>Panama,Panama</option>
<option>Panama Canal,Panama</option>
<option>Panama City,Panama</option>
<option>Panjang,Indonesia</option>
<option>Panyu,China</option>
<option>Papeete,Tahiti</option>
<option>Papsa,Panama</option>
<option>Paramaribo,Surinam</option>
<option>Paranagua,Brazil</option>
<option>Paris,France</option>
<option>Parma (Inland Point),Italy</option>
<option>Pasir Gudang,Malaysia</option>
<option>Patparganj,India</option>
<option>Pavlodar,Kazakhstan</option>
<option>Pearl River Delta,China</option>
<option>Pecem,Brazil</option>
<option>Pekanbaru,Indonesia</option>
<option>Pemba,Mozambique</option>
<option>Penang,Malaysia</option>
<option>Penghu,Guangdong Province</option>
<option>Perm,Russia</option>
<option>Perth,Australia</option>
<option>Peshawar,Pakistan</option>
<option>Petropavlosk,Russia</option>
<option>Philadelphia,Pennsylvania</option>
<option>Philipsburg,ST. Maarten</option>
<option>Phnom Penh,Cambodia</option>
<option>Phoenix,United States</option>
<option>Phuoc Long,Vietnam</option>
<option>Pilar,Argentina</option>
<option>Pinghai,Guangdong Province</option>
<option>Pingzhou,Hunan Province</option>
<option>Pipavav,India</option>
<option>Piraeus,Greece</option>
<option>Pisa,Italy</option>
<option>Pittsburgh,Pennsylvania</option>
<option>Ploce,Croatia</option>
<option>Plymouth,Trinidad</option>
<option>Podgorica,Montenegro</option>
<option>Pohang,South Korea</option>
<option>Pohnpei,Micronesia Islands</option>
<option>Point A Pitre,Guadeloupe</option>
<option>Point Lisas,Trinidad</option>
<option>Pointe Blanche,Caribbean</option>
<option>Pointe Des Galets,Reunion Islands</option>
<option>Pointe Noire,Congo</option>
<option>Pointe-A-Pitre,Leeward Island</option>
<option>Pomezia,Italy</option>
<option>Ponce,Puerto Rico</option>
<option>Pontianak,Indonesia</option>
<option>Pori,Finland</option>
<option>Port Alma,Queensland</option>
<option>Port Cabello,Venezuela</option>
<option>Port Chalmers,New Zealand</option>
<option>Port Des Galets,Africa</option>
<option>Port Elizabeth,South Africa</option>
<option>Port Everglades,Florida</option>
<option>Port Gentil,Gabon</option>
<option>Port Harcourt,Nigeria</option>
<option>Port Hedland,Australia</option>
<option>Port Kasim,Pakistan</option>
<option>Port Kembla,Australia</option>
<option>Port Klang,Malaysia</option>
<option>Port Klang (North),Malaysia</option>
<option>Port Klang (West),Malaysia</option>
<option>Port Limon,Costa Rica</option>
<option>Port Lisas,Panama</option>
<option>Port Louis,Mauritius Is.</option>
<option>Port Moresby,Papua New Guinea</option>
<option>Port Muhammad Bin Qasim,India</option>
<option>Port Noire,Congo</option>
<option>Port of Spain,Trinidad</option>
<option>Port Pirie,South Australia</option>
<option>Port Qasim,Pakistan</option>
<option>Port Rashid,United Arab Emirates</option>
<option>Port Reunion,South Africa</option>
<option>Port Said,Egypt</option>
<option>Port Sousse,Tunisia</option>
<option>Port Sudan,Sudan</option>
<option>Port Suez,Egypt</option>
<option>Port Sultan Qaboos,Oman</option>
<option>Port Victoria,East Africa</option>
<option>Port Vila,Vanuatu</option>
<option>Port-Au-Prince,Haiti</option>
<option>Portland,Oregon</option>
<option>Porto,Portugal</option>
<option>Porto Alegre,Brazil</option>
<option>Portsmouth,Virginia</option>
<option>Posorja,Ecuador</option>
<option>Poti,Georgia</option>
<option>Potianak,Indonesia</option>
<option>Poznan,Poland</option>
<option>Prague,Czech Republic</option>
<option>Praia,Cape Varde</option>
<option>Praia Mole,Brazil</option>
<option>Prato (Inland Point),Italy</option>
<option>Pretoria,Mozambique</option>
<option>Prince Rupert,Canada</option>
<option>Prishtina,Serbia</option>
<option>Pristina,Kosovo</option>
<option>Progreso,Mexico</option>
<option>Providence,Kentucky</option>
<option>Provinciales,Provinciales</option>
<option>Pskov,Russia</option>
<option>Pudong,Jiangsu Province</option>
<option>Pudong,Shanghai</option>
<option>Puerto Angamos,Peru</option>
<option>Puerto Armuelles,Panama</option>
<option>Puerto Bolivar,Colombia</option>
<option>Puerto Cabello,Venezuela</option>
<option>Puerto Caldera,Costa Rica</option>
<option>Puerto Coronel,Chile</option>
<option>Puerto Cortes,Honduras</option>
<option>Puerto Limon,Costa Rica</option>
<option>Puerto Madryn,Argentina</option>
<option>Puerto Moin,United States</option>
<option>Puerto Montt,Chile</option>
<option>Puerto Morelos,Mexico</option>
<option>Puerto Plata,Dominican Republic</option>
<option>Puerto Quetzal (San Jose),Guatemala</option>
<option>Puerto Sucre,Venezuela</option>
<option>Puinhon,Vietnam</option>
<option>Pune,India</option>
<option>Puning,Guangdong Province</option>
<option>Punta Arenas,Chile</option>
<option>Puntarenas,Costa Rica</option>
<option>Puqi,Zhejiang Province</option>
<option>Putian,Fujian Province</option>
<option>Pyeongtaek,South Korea</option>
<option>Qesim Island,United Arab Emirates</option>
<option>Qingdao,Shandong Province</option>
<option>Qingpu,Shanghai</option>
<option>Qingyuan,Guangdong Province</option>
<option>Qinhuangdao,Hebei Province</option>
<option>Qinzhou,Guangxi Province</option>
<option>Quang Ninh,Vietnam</option>
<option>Quanzhou,Fujian Province</option>
<option>Quelimane,Mozambique</option>
<option>Queretaro,Mexico</option>
<option>Quertaro,Mexico</option>
<option>Quezaltenango,Guatemala</option>
<option>Quinhon,Vietnam</option>
<option>Quito,Ecuador</option>
<option>Quzai,Lebanon</option>
<option>Quzhou,Zhejiang Province</option>
<option>Rabaul,Papua New Guinea</option>
<option>Radom,Poland</option>
<option>Raleigh,North Carolina</option>
<option>Rarotonga,Cook Islands</option>
<option>Ras Al Khaimah,United Arab Emirates</option>
<option>Ras Lanuf,Libya</option>
<option>Rauma,Finland</option>
<option>Ravenna,Italy</option>
<option>Rayong,Thailand</option>
<option>Recife,Brazil</option>
<option>Regina,Italy</option>
<option>Reunion,Reunion Islands</option>
<option>Reykjavik,Iceland</option>
<option>Richards Bay,South Africa</option>
<option>Richmond,Virginia</option>
<option>Ried,Austria</option>
<option>Riga,Latvia</option>
<option>Rijeka,Croatia</option>
<option>Rio de Janeiro,Brazil</option>
<option>Rio Grande,Brazil</option>
<option>Rio Grande (A),Argentina</option>
<option>Rio Grande Do Sul,Brazil</option>
<option>Rio Haina,Dominican Republic</option>
<option>Riyadh,Saudi Arabia</option>
<option>Rizhao,Shandong Province</option>
<option>Roadtown,Tortola</option>
<option>Roanne,France</option>
<option>Rochelle,United States</option>
<option>Rodman,Panama</option>
<option>Roenoe,Denmark</option>
<option>Rome,Italy</option>
<option>Rongqi,Guangdong Province</option>
<option>Rosario,Argentina</option>
<option>Rosarito,Mexico</option>
<option>Roseau,Dominica</option>
<option>Rostock,Germany</option>
<option>Rostov,Georgia</option>
<option>Rotorua,New Zealand</option>
<option>Rotterdam,Netherlands</option>
<option>Rouen,France</option>
<option>Rovno,Russia</option>
<option>Rudong,Jiangsu Province</option>
<option>Ruian,Zhejiang Province</option>
<option>Russe,Bulgaria</option>
<option>Russia,Russia</option>
<option>Rwanda,Africa</option>
<option>Ryazanj,Russia</option>
<option>Rzeszow,Poland</option>
<option>S. Vicente,Cape Varde</option>
<option>Sacramento,California</option>
<option>Saint-Etienne,France</option>
<option>Saipan,Marina Islands</option>
<option>Sakaiminato,Japan</option>
<option>Sakaisenboku,Japan</option>
<option>Sakata,Japan</option>
<option>Sakhalin,Russia</option>
<option>Salalah,Oman</option>
<option>Salerno,Italy</option>
<option>Salina Cruz,Mexico</option>
<option>Salomague,Philippines</option>
<option>Salonica,Greece</option>
<option>Salonika,Tanzania</option>
<option>Salt Lake City,United States</option>
<option>Salvador,Brazil</option>
<option>Salzburg,Austria</option>
<option>Samara,Russia</option>
<option>Samarinda,Indonesia</option>
<option>Samarkand,Russia</option>
<option>Sambeimen,Guangdong Province</option>
<option>Samsun,Turkey</option>
<option>San Antonio,Chile</option>
<option>San Antonio (TX),Texas</option>
<option>San Diego,California</option>
<option>San Felix,Chile</option>
<option>San Francisco,California</option>
<option>San Jose,Costa Rica</option>
<option>San Juan,Puerto Rico</option>
<option>San Lorenzo,Honduras</option>
<option>San Luis Colorado,Colorado</option>
<option>San Luis Potosi,Mexico</option>
<option>San Pedro,Argentina</option>
<option>San Pedro Sula,Honduras</option>
<option>San Salvador,Republic of El Salvador</option>
<option>San Vicente,Chile</option>
<option>Sana,Yemen</option>
<option>Sanbeimen,Guangdong Province</option>
<option>Sanbu,Guangdong Province</option>
<option>Sandakan, Sabah,Malaysia</option>
<option>Sanrong,Guangdong Province</option>
<option>Sanshan,Guangdong Province</option>
<option>Sanshui,Guangdong Province</option>
<option>Santa Cruz de Tenerife,Canary Islands</option>
<option>Santa Marta,Colombia</option>
<option>Santiago,Chile</option>
<option>Santo,Vanuatu</option>
<option>Santo Domingo,Dominican Republic</option>
<option>Santo Tomas de Castilla,Guatemala</option>
<option>Santos,Brazil</option>
<option>Sanya,Hainan Province</option>
<option>Sao Francisco Do Sul,Brazil</option>
<option>Sao Paulo,Brazil</option>
<option>Sao Tome,Western Africa</option>
<option>Sarajevo,Bosnia Hercegovina</option>
<option>Sarikei,Malaysia</option>
<option>Saskatoon,Canada</option>
<option>Savador Bahia,Brazil</option>
<option>Savannah,Georgia</option>
<option>Savannakhet,Laos</option>
<option>Savona,Italy</option>
<option>Savu Savu,Fiji Island</option>
<option>Seattle,Washington</option>
<option>Segoro,Indonesia</option>
<option>Semarang,Indonesia</option>
<option>Senboku,Japan</option>
<option>Sendai,Japan</option>
<option>Sens,France</option>
<option>Seoul,South Korea</option>
<option>Sepetiba,Brazil</option>
<option>Sete,France</option>
<option>Setubal,Portugal</option>
<option>Seward,Alaska</option>
<option>Sfax,Tunisia</option>
<option>Shangchuan Dao,China</option>
<option>Shangdong,Shandong Province</option>
<option>Shanghai,China</option>
<option>Shangqiu,Henan Province</option>
<option>Shantou,Guangdong Province</option>
<option>Shanwei,Guangdong Province</option>
<option>Shaoguan,Guangdong Province</option>
<option>Shaoxing,Zhejiang Province</option>
<option>Sharjah,United Arab Emirates</option>
<option>Shashi,Hubei Province</option>
<option>Shatian,Guangdong Province</option>
<option>Sheerness,U.K.</option>
<option>Shekou,Guangdong Province</option>
<option>Shenwan,Guangdong Province</option>
<option>Shenyang,Liaoning Province</option>
<option>Shenzhen,Guangdong Province</option>
<option>Shibushi,Japan</option>
<option>Shidao,Shandong Province</option>
<option>Shijiazhuang,Hebei Province</option>
<option>Shiliugang,Guangdong Province</option>
<option>Shima,Japan</option>
<option>Shimizu,Japan</option>
<option>Shimonoseki,Japan</option>
<option>Shiqi,Guangdong Province</option>
<option>Shiqiao (Pan Yu),Guangdong Province</option>
<option>Shishi,Fujian Province</option>
<option>Shitang,Guangdong Province</option>
<option>Shiwan,Guangdong Province</option>
<option>Shuaibah,Kuwait</option>
<option>Shuidong,Guangdong Province</option>
<option>Shuikou,Guangdong Province</option>
<option>Shunde,Guangdong Province</option>
<option>Shuwaikh,Kuwait</option>
<option>Sialkot,Pakistan</option>
<option>Siam,Thailand</option>
<option>Sibu, Sarawak,Malaysia</option>
<option>Sichuan,Sichuan Province</option>
<option>Sihanoukville,Cambodia</option>
<option>Sihui,Guangdong Province</option>
<option>Sines,Portugal</option>
<option>Singapore,Singapore</option>
<option>Sipitang,Malaysia</option>
<option>Skikda,Algeria</option>
<option>Skopje,Macedonia</option>
<option>Smolensk,Russia</option>
<option>Sochi,Russia</option>
<option>Socola,Romania</option>
<option>Sofia,Bulgaria</option>
<option>Sohar,Oman</option>
<option>Sokhna,Egypt</option>
<option>Somalia,Africa</option>
<option>Songkhla,Thailand</option>
<option>Sousse,Tunisia</option>
<option>South Caicos,Turks & Caicos</option>
<option>South Shields,U.K.</option>
<option>Southampton,U.K.</option>
<option>Sovgavanj,Russia</option>
<option>Soyo,Angola</option>
<option>Sparrow Point,Maryland</option>
<option>Split,Croatia</option>
<option>Sri Racha (Bangkok),Thailand</option>
<option>St. Barthelemy,Guadeloupe</option>
<option>St. Croix,Virgin Islands</option>
<option>St. Domingo,United States</option>
<option>St. George's,Grenada</option>
<option>St. Johns,Antigua</option>
<option>St. Louis,Missouri</option>
<option>St. Lucia,West Indies</option>
<option>St. Maarten,Caribbean</option>
<option>St. Petersburg,Russia</option>
<option>St. Polten,Austria</option>
<option>St. Thomas,Virgin Islands</option>
<option>Stockholm,Sweden</option>
<option>Stockton,California</option>
<option>Stoughton,United States</option>
<option>Stuttgart,Germany</option>
<option>Su Wan Na Kaed,Vietnam</option>
<option>Suape,Brazil</option>
<option>Subic Bay,Philippines</option>
<option>Suez Canal,Egypt</option>
<option>Suigang,Hunan Province</option>
<option>Sukhna,Egypt</option>
<option>Surabaya,Indonesia</option>
<option>Surat,India</option>
<option>Surgut,Russia</option>
<option>Suva,Fiji Island</option>
<option>Suzhou,Jiangsu Province</option>
<option>Svobodny,Russia</option>
<option>Swaziland,Africa</option>
<option>Sydney,Australia</option>
<option>Szczecin,Poland</option>
<option>Ta Kaek,Vietnam</option>
<option>Ta Na Lang,Vietnam</option>
<option>Tacoma,Washington</option>
<option>Taicang,Jiangsu Province</option>
<option>Taichung,China Taiwan</option>
<option>Taijiang,Fujian Province</option>
<option>Taipei,China Taiwan</option>
<option>Taiping,Guangdong Province</option>
<option>Taishan,Guangdong Province</option>
<option>Taiwan,China Taiwan</option>
<option>Taiyuan,Shanxi Province</option>
<option>Taizhou,Zhejiang Province</option>
<option>Takamatsu,Japan</option>
<option>Takoradi,Ghana</option>
<option>Talcahuano,Chile</option>
<option>Taldykorgan,Kazakhstan</option>
<option>Tallinn,Estonia</option>
<option>Tamatave,Madagascar</option>
<option>Tampa,Florida</option>
<option>Tampere,Finland</option>
<option>Tampico,Mexico</option>
<option>Tancang,Vietnam</option>
<option>Tanga,Tanzania</option>
<option>Tanger-Med,Morocco</option>
<option>Tanggu,Tianjin</option>
<option>Tangier,Morocco</option>
<option>Tangshan,Hebei Province</option>
<option>Tanjung Emas,Indonesia</option>
<option>Tanjung Manis,Malaysia</option>
<option>Tanjung Pelepas,Malaysia</option>
<option>Tao Yuan,China Taiwan</option>
<option>Taranto,Italy</option>
<option>Tarawa,Kirbati</option>
<option>Tarnobrzeg,Poland</option>
<option>Tarragona,Spain</option>
<option>Tashkent,Uzbekistan</option>
<option>Tauranga,New Zealand</option>
<option>Tawau,Malaysia</option>
<option>Tbilisi,Georgia</option>
<option>Tcbuen,Colombia</option>
<option>Tecate,Mexico</option>
<option>Teesport,U.K.</option>
<option>Tegucigalpa,Honduras</option>
<option>Tekirdag,Turkey</option>
<option>Tel Aviv,Israel</option>
<option>Tema,Ghana</option>
<option>Tenerife,Canary Islands</option>
<option>Teplice,Czech Republic</option>
<option>Tequcigalpa,Honduras</option>
<option>Terespol,Poland</option>
<option>Terport,Paraguay</option>
<option>Thamesport,U.K.</option>
<option>The Valley,Anguilla</option>
<option>Thessaloniki,Greece</option>
<option>Thilawa,Burma</option>
<option>Tijuana,Mexico</option>
<option>Tilbury,U.K.</option>
<option>Timaru,New Zealand</option>
<option>Tincan,Nigeria</option>
<option>Tinian,Micronesia Islands</option>
<option>Tirana,Albania</option>
<option>Toamasina,Madagascar</option>
<option>Tobata,Japan</option>
<option>Tobruk,Africa</option>
<option>Togliatti,Russia</option>
<option>Tokmak,Kyrgyzstan</option>
<option>Tokushima,Japan</option>
<option>Tokuyama,Japan</option>
<option>Tokyo,Japan</option>
<option>Toljati,Russia</option>
<option>Tomakomai,Japan</option>
<option>Tomsk,Russia</option>
<option>Tongan,Fujian Province</option>
<option>Tonglin,Anhui Province</option>
<option>Tonglu,Zhejiang Province</option>
<option>Tongshen,Hubei Province</option>
<option>Torghundi,Afghanistan</option>
<option>Toronto,Ontario</option>
<option>Torres Strait,Australia</option>
<option>Torun,Poland</option>
<option>Tosu,Japan</option>
<option>Townsville,Australia</option>
<option>Toyama,Japan</option>
<option>Toyamashiniko,Japan</option>
<option>Toyohashi,Japan</option>
<option>Toytepa,Uzbekistan</option>
<option>Trabzon,Turkey</option>
<option>Trieste,Italy</option>
<option>Trinidad,Caribbean</option>
<option>Tripoli,Libya</option>
<option>Trizt,Turkey</option>
<option>Troyes,France</option>
<option>Truk,Marina Islands</option>
<option>Tsuruga,Japan</option>
<option>Tulear,Madagascar</option>
<option>Tumen,Jilin Province</option>
<option>Tunis,Tunisia</option>
<option>Turgundi,Russia</option>
<option>Turku,Finland</option>
<option>Tuticorin,India</option>
<option>Tynda,Russia</option>
<option>Tyumen,Russia</option>
<option>Ube,Japan</option>
<option>Ufa,Russia</option>
<option>Ujung Pandang,Indonesia</option>
<option>Ulaan Baatar,Mongolia</option>
<option>Ulan Ude,Russia</option>
<option>Uljanovsk,Russia</option>
<option>Ulm,Germany</option>
<option>Ulsan,South Korea</option>
<option>Umm Qasr,Iraq</option>
<option>Uralsk,Kazakhstan</option>
<option>Urumqi,Xinjiang Province</option>
<option>Ushuaia,Argentina</option>
<option>Ussuryisk,Russia</option>
<option>Ust-Kamenogorsk,Kazakhstan</option>
<option>Vainikkala,Finland</option>
<option>Valence,France</option>
<option>Valencia,Spain</option>
<option>Valletta,Malta</option>
<option>Valparaiso,Chile</option>
<option>Vancouver,British Columbia</option>
<option>Vanino,Russia</option>
<option>Varna,Bulgaria</option>
<option>Vavau,Tonga</option>
<option>Venezia,Italy</option>
<option>Venice,Italy</option>
<option>Vennica,Russia</option>
<option>Vera Cruz,Mexico</option>
<option>Verino,Russia</option>
<option>Vernon,United States</option>
<option>Vesoul,France</option>
<option>Vict,Vietnam</option>
<option>Victoria,Argentina</option>
<option>Victoria (E.Africa),Seychelles</option>
<option>Vienna,Austria</option>
<option>Vientiane,Laos</option>
<option>Vieux Fort,Guadeloupe</option>
<option>Vigo,Spain</option>
<option>Vila,Vanuatu</option>
<option>Vila Do Conde,Brazil</option>
<option>Villa Nueva,Honduras</option>
<option>Vilnius,Lithuania</option>
<option>Virgin Gorda,Caribbean</option>
<option>Visakhapatnam,India</option>
<option>Vitebsk,Russia</option>
<option>Vitoria,Brazil</option>
<option>Vizag,India</option>
<option>Vladivostok,Russia</option>
<option>Vohemar,Madagascar</option>
<option>Volgogard,Russia</option>
<option>Vologda,Russia</option>
<option>Volos,Greece</option>
<option>Voltri,Italy</option>
<option>Voronez,Russia</option>
<option>Vostochny,Russia</option>
<option>Vungtau,Vietnam</option>
<option>Wai Gao Qiao,Shanghai</option>
<option>Wakayama,Japan</option>
<option>Wallis/Futuna,Micronesia Islands</option>
<option>Walvis Bay,Namiba</option>
<option>Wanganui,New Zealand</option>
<option>Wanzai (Zhuhai),Guangdong Province</option>
<option>Warren,Ohio</option>
<option>Warri,Nigeria</option>
<option>Warsaw,Poland</option>
<option>Wasilla,Alaska</option>
<option>Weifang,Shandong Province</option>
<option>Weihai,Shandong Province</option>
<option>Weitou,Fujian Province</option>
<option>Wellington,New Zealand</option>
<option>Wenzhou,Zhejiang Province</option>
<option>West Palm Beach,Florida</option>
<option>Wewak,Papua New Guinea</option>
<option>Whangarei,New Zealand</option>
<option>Whitestown,United States</option>
<option>Wilhelmshaven,Germany</option>
<option>Willemstad,Netherlands Antilles</option>
<option>Wilmington,North Carolina</option>
<option>Winnipeg,Canada</option>
<option>Wloclawek,Poland</option>
<option>Wolow,Poland</option>
<option>Wroclaw,Poland</option>
<option>Wuchun,Guangdong Province</option>
<option>Wuhan,Hubei Province</option>
<option>Wuhu,Anhui Province</option>
<option>Wujiang,Jiangsu Province</option>
<option>Wulumuqi,Xinjiang Province</option>
<option>Wumen,Zhejiang Province</option>
<option>Wuxi,Jiangsu Province</option>
<option>Wuzhou,Guangxi Province</option>
<option>Xanshi,China</option>
<option>Xiamen,Fujian Province</option>
<option>Xian,Shaanxi Province</option>
<option>Xiandria,China</option>
<option>Xiangtan,Hunan Province</option>
<option>Xiangyu,Xiamen</option>
<option>Xiangzhou,Guangdong Province</option>
<option>Xianyang,Shaanxi Province</option>
<option>Xiao Cuo,Fujian Province</option>
<option>Xiaogan,Hubei Province</option>
<option>Xiaohudao,Guangdong Province</option>
<option>Xiaolan (Shi Qi),Guangdong Province</option>
<option>Xiaoshan,Zhejiang Province</option>
<option>Xin Sha,Guangdong Province</option>
<option>Xinfeng,Guangdong Province</option>
<option>Xingang,Tianjin</option>
<option>Xinhui,Guangdong Province</option>
<option>Xining,Qinghai Province</option>
<option>Xintang,Guangdong Province</option>
<option>Xinyou,Fujian Province</option>
<option>Xiuhui,Guangdong Province</option>
<option>Xiuyu,Liaoning Province</option>
<option>Xuchang,Henan Province</option>
<option>Xuzhou,Jiangsu Province</option>
<option>Yakusk,Russia</option>
<option>Yangjiang,Guangdong Province</option>
<option>Yangon,Burma</option>
<option>Yangpu,Hainan Province</option>
<option>Yangshan,Shanghai</option>
<option>Yangzhou,Jiangsu Province</option>
<option>Yantai,Shandong Province</option>
<option>Yantian,Guangdong Province</option>
<option>Yap,Micronesia Islands</option>
<option>Yarimca,Turkey</option>
<option>Yatsushiro,Japan</option>
<option>Yawata,Japan</option>
<option>Yckaterinburg,Russia</option>
<option>Yeochon,South Korea</option>
<option>Yeosu,South Korea</option>
<option>Yeravan,Armenia</option>
<option>Yi Chang,Hubei Province</option>
<option>Yibin,Sichuan Province</option>
<option>Yinchuan,Ningxia Province</option>
<option>Yingkou,Liaoning Province</option>
<option>Yiwu,Zhejiang Province</option>
<option>Yixing,Jiangsu Province</option>
<option>Yokkaichi,Japan</option>
<option>Yokohama,Japan</option>
<option>Yokosuka,Japan</option>
<option>Yueyang,Hunan Province</option>
<option>Yunfu,Guangdong Province</option>
<option>Yunnan,Sichuan Province</option>
<option>Yuyao,Zhejiang Province</option>
<option>Zabaykalsk,Russia</option>
<option>Zagreb,Croatia</option>
<option>Zahony,Hungary</option>
<option>Zambia,Africa</option>
<option>Zamboanga,Philippines</option>
<option>Zanzibar,Tanzania</option>
<option>Zarate,Argentina</option>
<option>Zarqa Free Zone,Jordan</option>
<option>Zashita,Kazakhstan</option>
<option>Zeebrugge,Belgium</option>
<option>Zha Pu,Zhejiang Province</option>
<option>Zhangjiagang,Jiangsu Province</option>
<option>Zhangjiakou,Jiangsu Province</option>
<option>Zhangzhou,Fujian Province</option>
<option>Zhanjiang,Guangdong Province</option>
<option>Zhaogang,China</option>
<option>Zhaoqing,Guangdong Province</option>
<option>Zhaoqing New Port,Guangdong Province</option>
<option>Zhengzhou,Henan Province</option>
<option>Zhenjiang,Jiangsu Province</option>
<option>Zhenping,Henan Province</option>
<option>Zhezkazgan,Kazakhstan</option>
<option>Zhizhudao,Guangdong Province</option>
<option>Zhongshan,Guangdong Province</option>
<option>Zhongxinzhou,Guangdong Province</option>
<option>Zhoushan,Zhejiang Province</option>
<option>Zhoutouzui,Guangdong Province</option>
<option>Zhuhai,Guangdong Province</option>
<option>Zhuhai Port (Gaolan),Guangdong Province</option>
<option>Zhuzhou,Hunan Province</option>
<option>Zibo,Shandong Province</option>
<option>Zimbabwe,Africa</option>
<option>Zlin,Belgium</option>
<option>Zurich,Switzerland</option>
    </datalist>
    <input  autoComplete="on" list="suggestions"/> 
</div>
<body>
    <label for="Select PickUp Point"><h2>Select PickUp Point</h2></label>
    <select name="Select PickUp Point" id="Select PickUp Point" required>
      <option value="CFS">CFS</option>
      <option value="FACTORY">FACTORY</option>
      <option value="ICD">ICD</option>
      <option value="PORT">PORT</option>
    </select>
  </body>
    <div>
        <h2>Select Delivery ORIGIN</h2>
            <datalist id="suggestions" required>
        <option>Aachen,Germany</option>   
        <option>Aalesund,Denmark</option>
        <option>Aarhus,Denmark</option>
        <option>Abaco,Bahamas</option>
        <option>Abakan,Russia</option>
        <option>Abidjan,Ivory Coast</option>
        <option>Abu Dhabi,United Arab Emirates</option>
        <option>Aburatsu,Japan</option>
        <option>Acajutla,Republic of El Salvador</option>
        <option>Acapulco,Mexico</option>
        <option>Adabiya,Egypt</option>
        <option>Addis Ababa,Ethiopia</option>
        <option>Adelaide,South Australia</option>
        <option>Aden,Yemen</option>
        <option>Agadir,Morocco</option>
        <option>Agira (Inland Point),Italy</option>
        <option>Ahmedabad,India</option>
        <option>Ain Sokhna,Egypt</option>
        <option>Aitutaki,Cook Islands</option>
        <option>Ajman,United Arab Emirates</option>
        <option>Akita,Japan</option>
        <option>Akmola,Kazakhstan</option>
        <option>Aktau,Kazakhstan</option>
        <option>Aktobe,Kazakhstan</option>
        <option>Al Aqabah,Jordan</option>
        <option>AL Iskandariyah,Egypt</option>
        <option>AL Jubail,Saudi Arabia</option>
        <option>Al Khoms,Libya</option>
        <option>Alacahoyuk,Turkey</option>
        <option>Alashankou,Mongolia</option>
        <option>Alaska,United States</option>
        <option>Albany,United States</option>
        <option>Alexandria,Egypt</option>
        <option>Algeciras,Spain</option>
        <option>Algiers,Algeria</option>
        <option>Aliaga,Turkey</option>
        <option>Alicante,Spain</option>
        <option>Almaty,Kazakhstan</option>
        <option>Alotau,Papua New Guinea</option>
        <option>Alsancak,Turkey</option>
        <option>Altamira,Mexico</option>
        <option>Ambarli,Turkey</option>
        <option>Amman,Jordan</option>
        <option>Amsterdam,Netherlands</option>
        <option>An Ping,Guangdong Province</option>
        <option>Anacortes,Washington</option>
        <option>Anchorage,Alaska</option>
        <option>Ancona,Italy</option>
        <option>Anderson,South Carolina</option>
        <option>Angamos,Chile</option>
        <option>Annaba,Algeria</option>
        <option>Anqing,Anhui Province</option>
        <option>Anshun,Guizhou Province</option>
        <option>Antalya,Turkey</option>
        <option>Antigua,Guatemala</option>
        <option>Antofagasta,Chile</option>
        <option>Antwerp,Belgium</option>
        <option>Anzherskaya,Russia</option>
        <option>Aotou,Guangdong Province</option>
        <option>Apapa,Nigeria</option>
        <option>Apia,Western Samoa</option>
        <option>Aqaba,Jordan</option>
        <option>Aqaba Zerka Free Zone,Jordan</option>
        <option>Archangelsk,Russia</option>
        <option>Arica,Chile</option>
        <option>Arieki,Malaysia</option>
        <option>Aruba,Netherlands Antilles</option>
        <option>Ashdod,Israel</option>
        <option>Ashgabat,Turkmenistan</option>
        <option>Ashkelon,Israel</option>
        <option>Ashkhabad,Russia</option>
        <option>Asmara,Ethiopia</option>
        <option>Assab,Ethiopia</option>
        <option>Astana,Kazakhstan</option>
        <option>Astrakhan,Russia</option>
        <option>Asuncion,Paraguay</option>
        <option>Athens,Greece</option>
        <option>Atlanta,Georgia</option>
        <option>Atlixco,Mexico</option>
        <option>Atyrau,Kazakhstan</option>
        <option>Auckland,New Zealand</option>
        <option>Auxerre,France</option>
        <option>Avcilar,Turkey</option>
        <option>Avignon,France</option>
        <option>Azov,Russia</option>
        <option>Baghdad,Iraq</option>
        <option>Baguio,Philippines</option>
        <option>Bahama,Caribbean</option>
        <option>Bahrain,Persian Gulf</option>
        <option>Baku,Azerbaijan</option>
        <option>Balboa,Panama</option>
        <option>Balclutha,New Zealand</option>
        <option>Balikpapan,Indonesia</option>
        <option>Baltimore,Maryland</option>
        <option>Bamako,Mali</option>
        <option>Bangalore,India</option>
        <option>Bangbu,Anhui Province</option>
        <option>Bangkok,Thailand</option>
        <option>Bangkok (BMT),Thailand</option>
        <option>Bangkok (PAT),Thailand</option>
        <option>Bangkok (SCT),Thailand</option>
        <option>Bangkok (TPT),Thailand</option>
        <option>Bangkok (Unithai),Thailand</option>
        <option>Bangkok (UTCT),Thailand</option>
        <option>Bangpakong,Thailand</option>
        <option>Banjul,Gambia</option>
        <option>Baoan,Guangdong Province</option>
        <option>Baoying,Jiangsu Province</option>
        <option>Bar,Serbia</option>
        <option>Barcelona,Spain</option>
        <option>Bari,Italy</option>
        <option>Barnaul,Russia</option>
        <option>Barranquilla,Colombia</option>
        <option>Bartlett,United States</option>
        <option>Basamuk,Papua New Guinea</option>
        <option>Basel,Switzerland</option>
        <option>Basra,Iraq</option>
        <option>Basse-Terre,ST. Kitts</option>
        <option>Basuo,Hainan Province</option>
        <option>Bata,Equatorial Guinea</option>
        <option>Batam,Indonesia</option>
        <option>Batangas,Philippines</option>
        <option>Baton Rouge,Louisiana</option>
        <option>Batu Ampar,Indonesia</option>
        <option>Batumi,Georgia</option>
        <option>Beaumont,U.K.</option>
        <option>Beicun,Guangdong Province</option>
        <option>Beihai,Guangxi Province</option>
        <option>Beijiao,Guangdong Province</option>
        <option>Beijing,China</option>
        <option>Beira,Mozambique</option>
        <option>Beirut,Lebanon</option>
        <option>Bejaia,Algeria</option>
        <option>Belawan,Indonesia</option>
        <option>Belem,Brazil</option>
        <option>Belfast,Ireland</option>
        <option>Belgorad,Russia</option>
        <option>Belgrade,Serbia</option>
        <option>Belize,Belize</option>
        <option>Bell Bay,Australia</option>
        <option>Benete Bay,Indonesia</option>
        <option>Benghazi,Libya</option>
        <option>Benguela,Angola</option>
        <option>Beograd,Serbia</option>
        <option>Berbera,Somalia</option>
        <option>Berkakit,Russia</option>
        <option>Berlin,Germany</option>
        <option>Besancon,France</option>
        <option>Bielefeld,Germany</option>
        <option>Bilbao,Spain</option>
        <option>Bingazi,Libya</option>
        <option>Bintulu,Malaysia</option>
        <option>Birmingham,U.K.</option>
        <option>Birobidzhan,Russia</option>
        <option>Bishkek,Kyrgyzstan</option>
        <option>Bissau,Guinea</option>
        <option>Biysk,Russia</option>
        <option>Bizerte,Tunisia</option>
        <option>Blagoveschensk,Russia</option>
        <option>Blantyre,Malawi</option>
        <option>Blois,France</option>
        <option>Bluff,New Zealand</option>
        <option>Bobruysk,Russia</option>
        <option>Bogota,Colombia</option>
        <option>Bologna (Inland Point),Italy</option>
        <option>Boma,Zaire</option>
        <option>Bombay,India</option>
        <option>Bonaire,Netherlands</option>
        <option>Bonneuil Sur Marne,France</option>
        <option>Bordeaux,France</option>
        <option>Bosperus,Turkey</option>
        <option>Boston,Massachusetts</option>
        <option>Botswana,Africa</option>
        <option>Bourg,France</option>
        <option>Bratislava,Slovakia</option>
        <option>Bregenz,Austria</option>
        <option>Breinigsvolle,United States</option>
        <option>Bremen,Germany</option>
        <option>Bremerhaven,Germany</option>
        <option>Briansk,Russia</option>
        <option>Bridgetown,Barbados</option>
        <option>Brisbane,Australia</option>
        <option>Bristol,U.K.</option>
        <option>Brno,Czech Republic</option>
        <option>Brunei,Brunei</option>
        <option>Brunswick,Georgia</option>
        <option>Brussels,Belgium</option>
        <option>Brzeg Dolny,Poland</option>
        <option>Brzesc,Russia</option>
        <option>Bucharest,Romania</option>
        <option>Budapest,Hungary</option>
        <option>Buenaventura,Colombia</option>
        <option>Buenos Aires,Argentina</option>
        <option>Bufalo,Honduras</option>
        <option>Bugo,Philippines</option>
        <option>Bujumbuba,East Africa</option>
        <option>Bukavu,East Africa</option>
        <option>Bukhara,Russia</option>
        <option>Bulawayo,Zimbabwe</option>
        <option>Burgas,Bulgaria</option>
        <option>Burlington,New Jersey</option>
        <option>Burnie,Australia</option>
        <option>Busan,South Korea</option>
        <option>Busan/Pui,South Korea</option>
        <option>Bydgoszcz,Poland</option>
        <option>Caacupemi,Paraguay</option>
        <option>Cabedello,Brazil</option>
        <option>Cabinda,Angola</option>
        <option>Cadiz,Spain</option>
        <option>Cagayan de Oro,Philippines</option>
        <option>Cagliari,Italy</option>
        <option>Cai Mep,Vietnam</option>
        <option>Cailan,Vietnam</option>
        <option>Cairns,Queensland</option>
        <option>Cairo,Egypt</option>
        <option>Calabar,Nigeria</option>
        <option>Calcutta,India</option>
        <option>Caldera,Costa Rica</option>
        <option>Calgary,Alberta</option>
        <option>Callao,Peru</option>
        <option>Cambodia,Vietnam</option>
        <option>Cambridge,New Zealand</option>
        <option>Camden,U.K.</option>
        <option>Can Tho,Vietnam</option>
        <option>Canakkale,Turkey</option>
        <option>Canoas,Brazil</option>
        <option>Cantho,Vietnam</option>
        <option>Cao Fei Dian,Hebei Province</option>
        <option>Cape Town,South Africa</option>
        <option>Cape Verde,Africa</option>
        <option>Caracas,Venezuela</option>
        <option>Caribbean Islands,Caribbean</option>
        <option>Carson,United States</option>
        <option>Cartagena,Colombia</option>
        <option>Cartago,Colombia</option>
        <option>Casablanca,Morocco</option>
        <option>Castellon,Spain</option>
        <option>Castries,ST. Lucia</option>
        <option>Catania,Italy</option>
        <option>Caucedo,Dominican Republic</option>
        <option>Cavaglia (Inland Point),Italy</option>
        <option>Cayenne Fr.,Guyana</option>
        <option>Cebu,Philippines</option>
        <option>Ceuta,Morocco</option>
        <option>Chalon-Sur-Marne,France</option>
        <option>Chalon-Sur-Saone,France</option>
        <option>Chanaral,Chile</option>
        <option>Changchun,Jilin Province</option>
        <option>Changle,Fujian Province</option>
        <option>Changsha,Hunan Province</option>
        <option>Changshu,Jiangsu Province</option>
        <option>Changzhou,Jiangsu Province</option>
        <option>Chaohu,Anhui Province</option>
        <option>Chaozhou,Guangdong Province</option>
        <option>Charkov,Russia</option>
        <option>Charleston,South Carolina</option>
        <option>Charlestown,Nevis</option>
        <option>Charlotte,North Carolina</option>
        <option>Charlotte Amalie,ST. Thomas</option>
        <option>Chattanooga,Tennessee</option>
        <option>Chattogram,Bangladesh</option>
        <option>Cheljabinsk,Russia</option>
        <option>Chen Lian Ji,Hunan Province</option>
        <option>Chengdu,Sichuan Province</option>
        <option>Chenghai,Guangdong Province</option>
        <option>Chenglingji,Hunan Province</option>
        <option>Chennai,India</option>
        <option>Cherkassy,Ukraine</option>
        <option>Chiasso,Switzerland</option>
        <option>Chiba,Japan</option>
        <option>Chicago,Illinois</option>
        <option>Chimbote,Chile</option>
        <option>Chimkent,Kazakhstan</option>
        <option>Chingyuan,Henan Province</option>
        <option>Chistiansted,ST. Croix</option>
        <option>Chita,Russia</option>
        <option>Chittagong,Bangladesh</option>
        <option>Chiwan,Guangdong Province</option>
        <option>Choloma,Honduras</option>
        <option>Chongqing,China</option>
        <option>Christchurch,New Zealand</option>
        <option>Christiansted,ST. Croix</option>
        <option>Chu Lai,Vietnam</option>
        <option>Chuangsha,Jiangsu Province</option>
        <option>Chuansha,Shanghai</option>
        <option>Chuuk,Micronesia Islands</option>
        <option>Chymkent,Kyrgyzstan</option>
        <option>Cincinnati,Ohio</option>
        <option>Ciudad Del Este,Paraguay</option>
        <option>Civitavecchia,Italy</option>
        <option>Clermont-Ferrand,France</option>
        <option>Cleveland,Ohio</option>
        <option>Coatzacoalcos,Mexico</option>
        <option>Cochabamba,Bolivia</option>
        <option>Cochin,India</option>
        <option>Cocosolo,Panama</option>
        <option>Coega-Ngqura,South Africa</option>
        <option>Coimbatore,India</option>
        <option>Cologne,Germany</option>
        <option>Cologno Monzese (Inland Point),Italy</option>
        <option>Colombo,Sri Lanka</option>
        <option>Colon,Panama</option>
        <option>Columbus,Ohio</option>
        <option>Comores,India</option>
        <option>Conakry,Guinea</option>
        <option>Conception Bay,Chile</option>
        <option>Connellsville,United States</option>
        <option>Constanta,Romania</option>
        <option>Copenhagen,Denmark</option>
        <option>Coquimbo,Chile</option>
        <option>Cordoba,Argentina</option>
        <option>Corinto,Nicaragua</option>
        <option>Cork,Ireland</option>
        <option>Coronel,Chile</option>
        <option>Corpus Christi,United States</option>
        <option>Corsicana,Texas</option>
        <option>Cotabato,Philippines</option>
        <option>Cotonou,Benin</option>
        <option>Cremona (Inland Point),Italy</option>
        <option>Cristobal,Panama</option>
        <option>Cuemavaca,Mexico</option>
        <option>Cuenca,Spain</option>
        <option>Curacao,Curacao</option>
        <option>Curitiba,Brazil</option>
        <option>Czestochowa,Poland</option>
        <option>Da Chan Bay,Guangdong Province</option>
        <option>Dachen,Zhejiang Province</option>
        <option>Dadri,India</option>
        <option>Daesan,South Korea</option>
        <option>Dafeng,Jiangsu Province</option>
        <option>Daganwei (Guangzhou),Guangdong Province</option>
        <option>Dakar,Senegal</option>
        <option>Dalian,Liaoning Province</option>
        <option>Dallas,Texas</option>
        <option>Dalta Port,Egypt</option>
        <option>Damietta,Egypt</option>
        <option>Dammam,Saudi Arabia</option>
        <option>Dampier,Australia</option>
        <option>Danang,Vietnam</option>
        <option>Dandong,Liaoning Province</option>
        <option>Dapeng,Guangdong Province</option>
        <option>Dar es Salaam,Tanzania</option>
        <option>Darkhan,Mongolia</option>
        <option>Darwin,Australia</option>
        <option>Datian,Fujian Province</option>
        <option>Datong,Guangdong Province</option>
        <option>Davao,Philippines</option>
        <option>Dayabay,Guangdong Province</option>
        <option>Dekheila,Egypt</option>
        <option>Delhi,India</option>
        <option>Denver,Colorado</option>
        <option>Derince,Turkey</option>
        <option>Derna,Libya</option>
        <option>Destrehan,United States</option>
        <option>Detroit,Michigan</option>
        <option>Dhaka,Bangladesh</option>
        <option>Diego Suarez,Madagascar</option>
        <option>Dijon,France</option>
        <option>Dili,Timor</option>
        <option>Djen Djen,Algeria</option>
        <option>Djibouti,East Africa</option>
        <option>Dnepropetrovsk,Russia</option>
        <option>Do Ma Tou,Guangdong Province</option>
        <option>Doha,Qatar</option>
        <option>Dole,France</option>
        <option>Dominican,Dominican Republic</option>
        <option>Donetsk,Ukraine</option>
        <option>Dongguan,Guangdong Province</option>
        <option>Dongjiakou,Guangdong Province</option>
        <option>Dongjiangcang,Guangdong Province</option>
        <option>Dongshan,Fujian Province</option>
        <option>Dortmund,Germany</option>
        <option>Douala,Cameroon</option>
        <option>Doumen,Guangdong Province</option>
        <option>Dresden,Germany</option>
        <option>Druzba,Kazakhstan</option>
        <option>Dubai,United Arab Emirates</option>
        <option>Dublin,Ireland</option>
        <option>Duesseldorf,Germany</option>
        <option>Duisburg,Germany</option>
        <option>Dumyat,Egypt</option>
        <option>Dunedin,New Zealand</option>
        <option>Dunkerque,France</option>
        <option>Dunkirk,France</option>
        <option>Durban,South Africa</option>
        <option>Durres,Albania</option>
        <option>Dushanbe,Tajikistan</option>
        <option>Dusseldorf,Germany</option>
        <option>Dutch Harbor,United States</option>
        <option>Dzaoudzi,Mayotte</option>
        <option>Dzhezkazgan,Kazakhstan</option>
        <option>East Canada,Canada</option>
        <option>East London,South Africa</option>
        <option>Ebeye,Marina Islands</option>
        <option>Edincik,Turkey</option>
        <option>Edison,New Jersey</option>
        <option>Edmonton,Canada</option>
        <option>Ehoala,Madagascar</option>
        <option>Eilat,Israel</option>
        <option>Ekaterinburg,Russia</option>
        <option>El Dekhelia,Egypt</option>
        <option>El Guamache,Venezuela</option>
        <option>El Paso,Honduras</option>
        <option>El Progreso,Honduras</option>
        <option>El Salvador,Republic of El Salvador</option>
        <option>El-Dekheila,Egypt</option>
        <option>Embakasi,Kenya</option>
        <option>Encarnacion,Mexico</option>
        <option>Enping,Guangdong Province</option>
        <option>Ensenada,Mexico</option>
        <option>Erdenet,Mongolia</option>
        <option>Eren,Inner Mongolia</option>
        <option>Erlian,Inner Mongolia</option>
        <option>Esmeraldas,Ecuador</option>
        <option>Esperance,Australia</option>
        <option>Essen,Germany</option>
        <option>Estonia,Russia</option>
        <option>Everett,Washington</option>
        <option>Evyap Port,Turkey</option>
        <option>Exuma,Bahamas</option>
        <option>Famagusta,Cyprus</option>
        <option>Fangcheng,Guangxi Province</option>
        <option>Fangcun,Guangdong Province</option>
        <option>Felixstowe,U.K.</option>
        <option>Fenghua,Zhejiang Province</option>
        <option>Fenghuojiao (Tai Shan),Guangdong Province</option>
        <option>Fengxian,Jiangsu Province</option>
        <option>Fergana,Russia</option>
        <option>Fernandina Beach,Florida</option>
        <option>Florence,Italy</option>
        <option>Floroe,Norway</option>
        <option>Flushing,Netherlands</option>
        <option>Fontana,California</option>
        <option>Fort de France,Martinique</option>
        <option>Fortaleza,Brazil</option>
        <option>Fos Sur Mer,France</option>
        <option>Foshan,Guangdong Province</option>
        <option>Frankfurt,Germany</option>
        <option>Fredericia,Denmark</option>
        <option>Freeport,Bahamas</option>
        <option>Freetown,Sierra Leone</option>
        <option>Fremantle,Western Australia</option>
        <option>Fremont,California</option>
        <option>Frontroyal,Virginia</option>
        <option>Frunze,Russia</option>
        <option>Fujairah,United Arab Emirates</option>
        <option>Fukuoka,Japan</option>
        <option>Fukuyama,Japan</option>
        <option>Funafuti,Tuvalu</option>
        <option>Fuqing,Fujian Province</option>
        <option>Fuzhou,Fujian Province</option>
        <option>Gaborone,Botswana</option>
        <option>Galveston,Texas</option>
        <option>Gamagori,Japan</option>
        <option>Gaolan (Zhuhai),Guangdong Province</option>
        <option>Gaoming,Guangdong Province</option>
        <option>Gaosha,Guangdong Province</option>
        <option>Gaoyao,Guangdong Province</option>
        <option>Gaoyou,Jiangsu Province</option>
        <option>Gatemala City,Guatemala</option>
        <option>Gatun,Panama</option>
        <option>Gdansk,Poland</option>
        <option>Gdynia,Poland</option>
        <option>Gebze,Turkey</option>
        <option>Geelong,Australia</option>
        <option>Gemlik,Turkey</option>
        <option>General Santos City,Philippines</option>
        <option>Geneve,Switzerland</option>
        <option>Gennevilliers,France</option>
        <option>Genoa (Genova),Italy</option>
        <option>Geoje,South Korea</option>
        <option>George Town,Guyana</option>
        <option>Geraldton,Australia</option>
        <option>Ghazaouete,Algeria</option>
        <option>Ghent,Belgium</option>
        <option>Gibraltar,Spain</option>
        <option>Gijon,Spain</option>
        <option>Gioia Tauro,Italy</option>
        <option>Girdwood,Alaska</option>
        <option>Gladstone,Australia</option>
        <option>Glasgow,Scotland</option>
        <option>Gliwice,Poland</option>
        <option>Gomel,Russia</option>
        <option>Gongyi,Henan Province</option>
        <option>Gothenburg,Sweden</option>
        <option>Grand Rapids,United States</option>
        <option>Grand Turk,Caribbean</option>
        <option>Grangemouth,U.K.</option>
        <option>Grays,U.K.</option>
        <option>Graz,Austria</option>
        <option>Greensboro,North Carolina</option>
        <option>Guadalajara,Mexico</option>
        <option>Guam,Mariana Islands</option>
        <option>Guang Bao Tong,Guangdong Province</option>
        <option>Guangzhou,Guangdong Province</option>
        <option>Guanta,Venezuela</option>
        <option>Guarulhos,Brazil</option>
        <option>Guatemala City,Guatemala</option>
        <option>Guayaquil,Ecuador</option>
        <option>Guaymas,Mexico</option>
        <option>Guigang,Guangxi Province</option>
        <option>Guilin,Guangxi Province</option>
        <option>Guinea-Bissau,Western Africa</option>
        <option>Guiyang,Guizhou Province</option>
        <option>Guizhou,Guangdong Province</option>
        <option>Gustavia,ST. Barths</option>
        <option>Gwangyang,South Korea</option>
        <option>Hachinohe,Japan</option>
        <option>Hagen,Germany</option>
        <option>Haian,Hainan Province</option>
        <option>Haifa,Israel</option>
        <option>Haifeng,Guangdong Province</option>
        <option>Haikou,Hainan Province</option>
        <option>Haimen,Zhejiang Province</option>
        <option>Hainan,Fujian Province</option>
        <option>Haining,Zhejiang Province</option>
        <option>Haiphong,Vietnam</option>
        <option>Hairaton,Afghanistan</option>
        <option>Hairun,Fujian Province</option>
        <option>Haiti,Caribbean</option>
        <option>Haitian,Fujian Province</option>
        <option>Hakata,Japan</option>
        <option>Hakodate,Japan</option>
        <option>Haldia,India</option>
        <option>Halifax,Nova Scotia</option>
        <option>Hamad Port,Qatar</option>
        <option>Hamada,Japan</option>
        <option>Hamburg,Germany</option>
        <option>Hamilton,New Zealand</option>
        <option>Hamina,Finland</option>
        <option>Hangzhou,Zhejiang Province</option>
        <option>Hanjiang,Fujian Province</option>
        <option>Hankou,Hubei Province</option>
        <option>Hannover,Germany</option>
        <option>Hanoi,Vietnam</option>
        <option>Harare,Zimbabwe</option>
        <option>Harbin,Heilongjiang Province</option>
        <option>Hartford,Michigan</option>
        <option>Haydarpasa,Turkey</option>
        <option>Hazira,India</option>
        <option>Hebron,Ohio</option>
        <option>Hefei,Anhui Province</option>
        <option>Hehou (Xin Hui),Guangdong Province</option>
        <option>Helsingborg,Sweden</option>
        <option>Helsinki,Finland</option>
        <option>Hengyang,Hunan Province</option>
        <option>Herakleion,Greece</option>
        <option>Heshan,Guangdong Province</option>
        <option>Hialeah,United States</option>
        <option>Hibiki,Japan</option>
        <option>Hibikinada,Japan</option>
        <option>Higashiharima,Japan</option>
        <option>Hilo,Hawaii</option>
        <option>Himeji,Japan</option>
        <option>Hiroshima,Japan</option>
        <option>Hitachi,Japan</option>
        <option>Hitachinaka,Japan</option>
        <option>Ho Chi Minh (Catlai),Vietnam</option>
        <option>Ho Chi Minh (Newport),Vietnam</option>
        <option>Ho Chi Minh City,Vietnam</option>
        <option>Hobart,Australia</option>
        <option>Hodeidah,Yemen</option>
        <option>Hohhot,Inner Mongolia</option>
        <option>Hon Gai,Vietnam</option>
        <option>Hong Kong,Hong Kong</option>
        <option>Hongkou,Jiangsu Province</option>
        <option>Honiara,Solomon Islands</option>
        <option>Honolulu,Hawaii</option>
        <option>Hososhima,Japan</option>
        <option>Houston,Texas</option>
        <option>Hua Sai,Vietnam</option>
        <option>Huadu,Guangdong Province</option>
        <option>Huainan,Anhui Province</option>
        <option>Huang Dao,South Korea</option>
        <option>Huang Shi,Hubei Province</option>
        <option>Huanghua,Hebei Province</option>
        <option>Huangpu,Guangdong Province</option>
        <option>Huangqi,Fujian Province</option>
        <option>Huangshan,Anhui Province</option>
        <option>Huizhou,Guangdong Province</option>
        <option>Hull,U.K.</option>
        <option>Humen,Guangdong Province</option>
        <option>Huntington,United States</option>
        <option>Huntsville,United States</option>
        <option>Hyderabad,India</option>
        <option>Hyogo,Japan</option>
        <option>Ijmuiden,Netherlands</option>
        <option>Iligan,Philippines</option>
        <option>Illichivsk,Ukraine</option>
        <option>Ilo,Peru</option>
        <option>Ilyichevsk,Ukraine</option>
        <option>Imabari,Japan</option>
        <option>Imari,Japan</option>
        <option>Imbituba,Brazil</option>
        <option>Immingham,U.K.</option>
        <option>Inchon,South Korea</option>
        <option>Indianapolis,Indiana</option>
        <option>Innsbruck,Austria</option>
        <option>Innxv,India</option>
        <option>Invercargill,New Zealand</option>
        <option>Invergordon,Scotland</option>
        <option>Ipoh,Malaysia</option>
        <option>Ipswich,U.K.</option>
        <option>Iquique,Chile</option>
        <option>Irbid,Jordan</option>
        <option>Irkutsk,Russia</option>
        <option>Irun,Spain</option>
        <option>Ishigaki,Japan</option>
        <option>Ishikari,Japan</option>
        <option>Ishikariwan,Japan</option>
        <option>Ishino Maki,Japan</option>
        <option>Iskenderun,Turkey</option>
        <option>Islam Qala,Afghanistan</option>
        <option>Istanbul,Turkey</option>
        <option>Itaguai,Brazil</option>
        <option>Itajai,Brazil</option>
        <option>Itapetinga,Brazil</option>
        <option>Itapoa,Brazil</option>
        <option>Itaqui,Brazil</option>
        <option>Iwakuni,Japan</option>
        <option>Iyomishima,Japan</option>
        <option>Izmir,Turkey</option>
        <option>Izmit,Turkey</option>
        <option>Izmit Korfezi,Turkey</option>
        <option>Jacksonville,Florida</option>
        <option>Jaipur,India</option>
        <option>Jakarta,Indonesia</option>
        <option>Jakarta UTC1,Indonesia</option>
        <option>Jakarta UTC3,Indonesia</option>
        <option>Jawaharlal Nehru,India</option>
        <option>Jebel Ali,United Arab Emirates</option>
        <option>Jebel Ali Freezone,United Arab Emirates</option>
        <option>Jeddah,Saudi Arabia</option>
        <option>Jelenia Gora,Poland</option>
        <option>Jiading,Shanghai</option>
        <option>Jiamusi,Heilongjiang Province</option>
        <option>Jiang Tang,China</option>
        <option>Jiangmen,Guangdong Province</option>
        <option>Jiangyin,Jiangsu Province</option>
        <option>Jiankou,Fujian Province</option>
        <option>Jiaojiang,Zhejiang Province</option>
        <option>Jiaokou,Guangdong Province</option>
        <option>Jiaoxin,Guangdong Province</option>
        <option>Jiaxing,Zhejiang Province</option>
        <option>Jiazi (Lu Feng),Guangdong Province</option>
        <option>Jieyang,Guangdong Province</option>
        <option>Jinan,Shandong Province</option>
        <option>Jing Tang,Shandong Province</option>
        <option>Jingan,Guangdong Province</option>
        <option>Jinghua,Zhejiang Province</option>
        <option>Jingjiang,Jiangsu Province</option>
        <option>Jinguzhou,Guangdong Province</option>
        <option>Jinshan,Shanghai</option>
        <option>Jinzhou,Liaoning Province</option>
        <option>Jisi,Guangdong Province</option>
        <option>Jiujiang,Jiangxi Province</option>
        <option>Jiujiang (Nanhai),Guangdong Province</option>
        <option>Jiuzhou,Guangdong Province</option>
        <option>Johannesburg,South Africa</option>
        <option>Johor,Malaysia</option>
        <option>Jubail,Saudi Arabia</option>
        <option>Kabil,Indonesia</option>
        <option>Kabul,Afghanistan</option>
        <option>Kachkanar,Russia</option>
        <option>Kaduna,Nigeria</option>
        <option>Kagoshima,Japan</option>
        <option>Kahului,Hawaii</option>
        <option>Kaifeng,Henan Province</option>
        <option>Kaiping,Guangdong Province</option>
        <option>Kakinada,India</option>
        <option>Kakogawa,Japan</option>
        <option>Kaliningrad,Russia</option>
        <option>Kaluga,Russia</option>
        <option>Kam Pong Som,Cambodia</option>
        <option>Kamchatka,Russia</option>
        <option>Kampala,Uganda</option>
        <option>Kanazawa,Japan</option>
        <option>Kandahar,Afghanistan</option>
        <option>Kandla,India</option>
        <option>Kansas City,Kansas</option>
        <option>Kantang,Thailand</option>
        <option>Kaohsiung,China Taiwan</option>
        <option>Karachi,Pakistan</option>
        <option>Karaganda,Kazakhstan</option>
        <option>Karatsu,Japan</option>
        <option>Kashima,Japan</option>
        <option>Kassel,Germany</option>
        <option>Kathmandu,Nepal</option>
        <option>Katowice,Poland</option>
        <option>Kattupalli,India</option>
        <option>Kavieng,Papua New Guinea</option>
        <option>Kavkaz,Russia</option>
        <option>Kawaihae,Hawaii</option>
        <option>Kawasaki,Japan</option>
        <option>Kayes,Mali</option>
        <option>Kazan,Russia</option>
        <option>Kearny,New Jersey</option>
        <option>Keelung,China Taiwan</option>
        <option>Kemaman,Malaysia</option>
        <option>Kemerovo,Russia</option>
        <option>Kenai,Alaska</option>
        <option>Kent,United States</option>
        <option>Khabarovsk,Russia</option>
        <option>Khalifa,United Arab Emirates</option>
        <option>Kharkov,Ukraine</option>
        <option>Khartoum,Sudan</option>
        <option>Khasan,Russia</option>
        <option>Khoms,Africa</option>
        <option>Khor Fakkan,United Arab Emirates</option>
        <option>Khorol,Russia</option>
        <option>Khudjand,Kazakhstan</option>
        <option>Kiel,Germany</option>
        <option>Kielce,Poland</option>
        <option>Kiev,Ukraine</option>
        <option>Kimbe,Papua New Guinea</option>
        <option>Kimitsu,Japan</option>
        <option>King Abdullah,Saudi Arabia</option>
        <option>Kingston,Jamaica</option>
        <option>Kingstown,Saint Vincent</option>
        <option>Kinshasa,Zaire</option>
        <option>Kishinev,Russia</option>
        <option>Kismayu,Somalia</option>
        <option>Klagenfurt,Austria</option>
        <option>Klaipeda,Lithuania</option>
        <option>Kobe,Japan</option>
        <option>Kochi,Japan</option>
        <option>Kokura,Japan</option>
        <option>Kolkata,India</option>
        <option>Koln,Germany</option>
        <option>Koming,Guangdong Province</option>
        <option>Kompong Som,Cambodia</option>
        <option>Komsomolsk Na Amur,Russia</option>
        <option>Koper,Slovenia</option>
        <option>Koror,Palau</option>
        <option>Korsakov,Russia</option>
        <option>Koshichang,Japan</option>
        <option>Kosrae,Micronesia Islands</option>
        <option>Kota Kinabalu,Malaysia</option>
        <option>Kotka,Finland</option>
        <option>Krakow,Poland</option>
        <option>Krasnodar,Russia</option>
        <option>Krasnovosk,Russia</option>
        <option>Krasnoyarsk,Russia</option>
        <option>Kribi,Africa</option>
        <option>Krishnapatnam,India</option>
        <option>Kristiansand,Norway</option>
        <option>Kuala Lumpur,Malaysia</option>
        <option>Kuantan,Malaysia</option>
        <option>Kuching,Malaysia</option>
        <option>Kumamoto,Japan</option>
        <option>Kumport,Turkey</option>
        <option>Kunming,Yunnan Province</option>
        <option>Kunsan,South Korea</option>
        <option>Kunshan,Jiangsu Province</option>
        <option>Kure,Japan</option>
        <option>Kurgan,Russia</option>
        <option>Kursk,Russia</option>
        <option>KUSAN,South Korea</option>
        <option>Kushiro,Japan</option>
        <option>Kustany,Kazakhstan</option>
        <option>Kuwait,Persian Gulf</option>
        <option>Kuybyshev,Russia</option>
        <option>Kwajalein,Micronesia Islands</option>
        <option>Kwangyang,South Korea</option>
        <option>Kyoto,Japan</option>
        <option>La Ceiba,Honduras</option>
        <option>La Goulette,Tunisia</option>
        <option>La Guaira,Venezuela</option>
        <option>La Lima,Honduras</option>
        <option>La Paz,Bolivia</option>
        <option>La Spezia,Italy</option>
        <option>La Union,Republic of El Salvador</option>
        <option>Labuan,Malaysia</option>
        <option>Lae,Papua New Guinea</option>
        <option>Laem Chabang,Thailand</option>
        <option>Lagos/Apapa,Nigeria</option>
        <option>Lahat Datu,Malaysia</option>
        <option>Lahore,Pakistan</option>
        <option>Laizhou,Guangdong Province</option>
        <option>Lake Charles,United States</option>
        <option>Lancaster,California</option>
        <option>Lanshan,Henan Province</option>
        <option>Lanshi,Guangdong Province</option>
        <option>Lanxi,Guangdong Province</option>
        <option>Lanzhou,Gansu Province</option>
        <option>Laon,France</option>
        <option>Laos,Thailand</option>
        <option>Laredo,United States</option>
        <option>Larnaca,Cyprus</option>
        <option>Larvik,Norway</option>
        <option>Las Minas,Guatemala</option>
        <option>Las Palmas,Canary Islands</option>
        <option>Lat Krabang,Thailand</option>
        <option>Latvia,Russia</option>
        <option>Lautoka,Fiji Island</option>
        <option>Lawrence,Kansas</option>
        <option>Lazaro Cardenas,Mexico</option>
        <option>Le Havre,France</option>
        <option>Le Verdon,France</option>
        <option>Leeds,U.K.</option>
        <option>Leghorn (Livorno),Italy</option>
        <option>Leicester,U.K.</option>
        <option>Leipzig,Germany</option>
        <option>Leith,U.K.</option>
        <option>Leixoes,Portugal</option>
        <option>Leliu,Guangdong Province</option>
        <option>Leninabad,Russia</option>
        <option>Leon,Mexico</option>
        <option>Lerma,Spain</option>
        <option>Lerma Estado de Mexico,Mexico</option>
        <option>Lesotho,Maseru</option>
        <option>Levin,New Zealand</option>
        <option>Lianhuashan,Guangdong Province</option>
        <option>Lianyungang,Jiangsu Province</option>
        <option>Liaoning,China</option>
        <option>Libreville,Gabon</option>
        <option>Lihir,Papua New Guinea</option>
        <option>Lilongwe,Malawi</option>
        <option>Lima,Peru</option>
        <option>Limassol,Cyprus</option>
        <option>Limon,Costa Rica</option>
        <option>Linbai,Zhejiang Province</option>
        <option>Linkoping,Sweden</option>
        <option>Linyi,Shandong Province</option>
        <option>Linz,Austria</option>
        <option>Lipetsk,Russia</option>
        <option>Lirquen,Chile</option>
        <option>Lisbon,Portugal</option>
        <option>Lithuania,Russia</option>
        <option>Liudu,Guangdong Province</option>
        <option>Liuzhou,Guangxi Province</option>
        <option>Liverpool,U.K.</option>
        <option>Livorno,Italy</option>
        <option>Ljubljana,Slovenia</option>
        <option>Llyichevsk,Ukraine</option>
        <option>Lobito,Angola</option>
        <option>Lodz,Poland</option>
        <option>Lome,Togo</option>
        <option>London,U.K.</option>
        <option>London Gateway Port,U.K.</option>
        <option>Long Beach,California</option>
        <option>Long Island,Bahamas</option>
        <option>Longkou,Shandong Province</option>
        <option>Longoni,Africa</option>
        <option>Longtan,Jiangsu Province</option>
        <option>Loni,India</option>
        <option>Lorengau,Papua New Guinea</option>
        <option>Los Angeles,California</option>
        <option>Louisville,United States</option>
        <option>Luanda,Angola</option>
        <option>Lubango,Angola</option>
        <option>Lublin,Poland</option>
        <option>Lubljana,Slovenia</option>
        <option>Lubumbashi,Congo</option>
        <option>Ludhiana,India</option>
        <option>Ludiana,India</option>
        <option>Lumut,Indonesia</option>
        <option>Luoyang,Henan Province</option>
        <option>Lusaka,Zambia</option>
        <option>Luxembourg,Luxembourg</option>
        <option>Luzhou,Sichuan Province</option>
        <option>Lvov,Russia</option>
        <option>Lyon,France</option>
        <option>Lyttelton,New Zealand</option>
        <option>Ma An Shan,Anhui Province</option>
        <option>Maaloy,Norway</option>
        <option>Macau,China</option>
        <option>Maceio,Brazil</option>
        <option>Mackay,Queensland</option>
        <option>Macon,France</option>
        <option>Madagascar,Africa</option>
        <option>Madang,Papua New Guinea</option>
        <option>Madison,N.Y.</option>
        <option>Madras,India</option>
        <option>Madrid,Spain</option>
        <option>Maerak,Indonesia</option>
        <option>Mafang,Guangdong Province</option>
        <option>Magadan,Russia</option>
        <option>Magnitogorsk,Russia</option>
        <option>Mahajunga,Africa</option>
        <option>Mahe,Seychelles</option>
        <option>Mailiao,China Taiwan</option>
        <option>Maizuru,Japan</option>
        <option>Majunga,Madagascar</option>
        <option>Majuro,Marshall Islands</option>
        <option>Makasaar,Indonesia</option>
        <option>Malabo,Equatorial Guinea</option>
        <option>Malacca,Malaysia</option>
        <option>Malaga,Canary Islands</option>
        <option>Malawi,Africa</option>
        <option>Male,Maldves</option>
        <option>Malmo,Sweden</option>
        <option>Malongo,Angola</option>
        <option>Malta,Malta</option>
        <option>Managua,Nicaragua</option>
        <option>Manaus,Brazil</option>
        <option>Manchester,U.K.</option>
        <option>Mangalore,India</option>
        <option>Mangyshlak,Kazakhstan</option>
        <option>Manila (MICT),Philippines</option>
        <option>Manila (North),Philippines</option>
        <option>Manila (South),Philippines</option>
        <option>Mannheim,Germany</option>
        <option>Manta,Ecuador</option>
        <option>Manzanillo,Mexico</option>
        <option>Manzanillo (P),Panama</option>
        <option>Manzhouli,Inner Mongolia</option>
        <option>Maoming,Guangdong Province</option>
        <option>Maptaput,Thailand</option>
        <option>Maputo,Mozambique</option>
        <option>Mar Del Plata,Argentina</option>
        <option>Maracaibo,Venezuela</option>
        <option>Mardas,Turkey</option>
        <option>Margarita,Venezuela</option>
        <option>Mariupol,Russia</option>
        <option>Marmagao,India</option>
        <option>Marport,Turkey</option>
        <option>Marsa Ei Brega,Libya</option>
        <option>Marsaxlokk,Malta</option>
        <option>Marsdan Point,New Zealand</option>
        <option>Marseilles,France</option>
        <option>Marseilles-Fos,France</option>
        <option>Marsh Harbour,Bahamas</option>
        <option>Masan,South Korea</option>
        <option>Maseru,Lesotho</option>
        <option>Massawa,Ethiopia</option>
        <option>Matadi,Zaire</option>
        <option>Matarani,Peru</option>
        <option>Matsuyama,Japan</option>
        <option>Mauritius,Africa</option>
        <option>Mawan,Guangdong Province</option>
        <option>Mawei,Fujian Province</option>
        <option>Mayotte,Comores Islands</option>
        <option>Mazar-I-Sharif,Afghanistan</option>
        <option>Mcdondough,United States</option>
        <option>Medan,Indonesia</option>
        <option>Medeu,Kazakhstan</option>
        <option>Megion,Russia</option>
        <option>Mejillones,Chile</option>
        <option>Melbourne,Australia</option>
        <option>Melilla,Morocco</option>
        <option>Memphis,Tennessee</option>
        <option>Mendoza,Argentina</option>
        <option>Merak,Indonesia</option>
        <option>Meridian,United States</option>
        <option>Mersin,Turkey</option>
        <option>Mexicali,Mexico</option>
        <option>Mexico City,Mexico</option>
        <option>Miami,Florida</option>
        <option>Middlesbrough,U.K.</option>
        <option>Miike,Japan</option>
        <option>Milan (Inland Point),Italy</option>
        <option>Milwaukee,South Dakota</option>
        <option>Mina Qaboos,Persian Gulf</option>
        <option>Mindanao,Philippines</option>
        <option>Mindelo,Cape Varde</option>
        <option>Minneapolis,Minnesota</option>
        <option>Minnesota,United States</option>
        <option>Minsk,Russia</option>
        <option>Mira Loma,California</option>
        <option>Miri,Malaysia</option>
        <option>Miskolc,Hungary</option>
        <option>Mississauga,Canada</option>
        <option>Misurata,Libya</option>
        <option>Mizushima,Japan</option>
        <option>Mobile,Alabama</option>
        <option>Mogadiscio,Somalia</option>
        <option>Mogilev,Russia</option>
        <option>Moji,Japan</option>
        <option>Mokop,South Korea</option>
        <option>Mombasa,Kenya</option>
        <option>Mongla,Bangladesh</option>
        <option>Monrovia,Liberia</option>
        <option>Montego Bay,Jamaica</option>
        <option>Monterrey,Mexico</option>
        <option>Montevideo,Uruguay</option>
        <option>Montgomery,Maryland</option>
        <option>Montoir,France</option>
        <option>Montpellier,France</option>
        <option>Montreal,Quebec</option>
        <option>Montserrat,Caribbean</option>
        <option>Morehead City,North Carolina</option>
        <option>Mormagao,India</option>
        <option>Moroni,Comores Islands</option>
        <option>Morristown,Tennessee</option>
        <option>Morrisville,Pennsylvania</option>
        <option>Moscow,Russia</option>
        <option>Mostaganem,Algeria</option>
        <option>Motukea,Papua New Guinea</option>
        <option>Muara,Brunei</option>
        <option>Mucuripe,Brazil</option>
        <option>Mudanjiang,Heilongjiang Province</option>
        <option>Mukalla,South Yemen</option>
        <option>Mulund,India</option>
        <option>Mumbai,India</option>
        <option>Mundra,India</option>
        <option>Munich,Germany</option>
        <option>Muplu,Mauritius Is.</option>
        <option>Murmans,Russia</option>
        <option>Murmansk,Russia</option>
        <option>Muroran,Japan</option>
        <option>Muscat,Oman</option>
        <option>Mutare,Zimbabwe</option>
        <option>Mutsamudu,Comores Islands</option>
        <option>Nacala,Mozambique</option>
        <option>Nagasaki,Japan</option>
        <option>Nagoya,Japan</option>
        <option>Naha,Japan</option>
        <option>Nairobi,Kenya</option>
        <option>Nakanoseki,Japan</option>
        <option>Nakhodka,Russia</option>
        <option>Namangan,Uzbekistan</option>
        <option>Namibe,Angola</option>
        <option>Nanao,Guangdong Province</option>
        <option>Nanchang,Jiangxi Province</option>
        <option>Nangang (Nanhai),Guangdong Province</option>
        <option>Nanguang,Sichuan Province</option>
        <option>Nanhai,Guangdong Province</option>
        <option>Nanhai (Sanshan),Guangdong Province</option>
        <option>Nanhui,Shanghai</option>
        <option>Nanjing,Jiangsu Province</option>
        <option>Nankeng,Hunan Province</option>
        <option>Nanning,Guangxi Province</option>
        <option>Nansha (Guangzhou),Guangdong Province</option>
        <option>Nantong,Jiangsu Province</option>
        <option>Naoetsu,Japan</option>
        <option>Napier,New Zealand</option>
        <option>Naples,Italy</option>
        <option>Narathiwat,Thailand</option>
        <option>Nashville,Tennessee</option>
        <option>Nassau,Bahamas</option>
        <option>Nauru,Nauru</option>
        <option>Navegantes,Brazil</option>
        <option>Nawilwili,Hawaii</option>
        <option>Ndola,Zambia</option>
        <option>Nelson,New Zealand</option>
        <option>Nemrut Bay,Turkey</option>
        <option>Neryungri,Russia</option>
        <option>Nevers,France</option>
        <option>New Castle,U.K.</option>
        <option>New Delhi,India</option>
        <option>New Jersey,New Jersey</option>
        <option>New London,United States</option>
        <option>New Orleans,Louisiana</option>
        <option>New Plymouth,New Zealand</option>
        <option>New York,N.Y.</option>
        <option>New York Harbour,N.Y.</option>
        <option>Newark,New Jersey</option>
        <option>Newcastle,Australia</option>
        <option>Newport News,Virginia</option>
        <option>Ngqura,South Africa</option>
        <option>Nhatrang,Vietnam</option>
        <option>Nhava Sheva,India</option>
        <option>Nigqura,India</option>
        <option>Niigata,Japan</option>
        <option>Ningbo,Zhejiang Province</option>
        <option>Ningde,Fujian Province</option>
        <option>Niue,Cook Islands</option>
        <option>Nizhnevartovsk,Russia</option>
        <option>Nizhny Novgorod,Russia</option>
        <option>Nizhny Tagil,Russia</option>
        <option>Nogales,Mexico</option>
        <option>Nola,Italy</option>
        <option>Norfolk,Virginia</option>
        <option>Noro,Solomon Islands</option>
        <option>Norrkoping,Sweden</option>
        <option>Northlake,United States</option>
        <option>Nossi-Be,Madagascar</option>
        <option>Nosy Be,Madagascar</option>
        <option>Nottingham,U.K.</option>
        <option>Nouadhibou,Mauritania</option>
        <option>Nouakchott,Mauritania</option>
        <option>Noumea,New Caledonia</option>
        <option>Novgorod,Russia</option>
        <option>Novokuznetsk,Mexico</option>
        <option>Novorossiysk,Russia</option>
        <option>Novorosyjsk,Russia</option>
        <option>Novosibirsk,Russia</option>
        <option>Noyabrjsk,Russia</option>
        <option>Nsict,India</option>
        <option>Nuernberg,Germany</option>
        <option>Nuevo Laredo,Mexico</option>
        <option>Nukualofa,Tonga</option>
        <option>Oakland,California</option>
        <option>Oamaru,New Zealand</option>
        <option>Odessa,Ukraine</option>
        <option>Oita,Japan</option>
        <option>Okayama,Japan</option>
        <option>Okinawa,Japan</option>
        <option>Omaezaki,Japan</option>
        <option>Omaha,Nebraska</option>
        <option>Omsk,Russia</option>
        <option>Onahama,Japan</option>
        <option>Onne,Nigeria</option>
        <option>Onsan,South Korea</option>
        <option>Oporto,Portugal</option>
        <option>Oran,Algeria</option>
        <option>Oranjestad,Aruba</option>
        <option>Orlando,Florida</option>
        <option>Orleans,France</option>
        <option>Orobay,Papua New Guinea</option>
        <option>Orsa,Russia</option>
        <option>Orzea,Russia</option>
        <option>Osaka,Japan</option>
        <option>Osh,Kyrgyzstan</option>
        <option>Oslo,Norway</option>
        <option>Otake,Japan</option>
        <option>Otalu,Japan</option>
        <option>Otaru,Japan</option>
        <option>Oxford,U.K.</option>
        <option>Padang,Indonesia</option>
        <option>Pagny,France</option>
        <option>Pago Pago,American Samoa</option>
        <option>Paita,Peru</option>
        <option>Palembang,Indonesia</option>
        <option>Palermo,Italy</option>
        <option>Palmerston North,New Zealand</option>
        <option>Panama,Panama</option>
        <option>Panama Canal,Panama</option>
        <option>Panama City,Panama</option>
        <option>Panjang,Indonesia</option>
        <option>Panyu,China</option>
        <option>Papeete,Tahiti</option>
        <option>Papsa,Panama</option>
        <option>Paramaribo,Surinam</option>
        <option>Paranagua,Brazil</option>
        <option>Paris,France</option>
        <option>Parma (Inland Point),Italy</option>
        <option>Pasir Gudang,Malaysia</option>
        <option>Patparganj,India</option>
        <option>Pavlodar,Kazakhstan</option>
        <option>Pearl River Delta,China</option>
        <option>Pecem,Brazil</option>
        <option>Pekanbaru,Indonesia</option>
        <option>Pemba,Mozambique</option>
        <option>Penang,Malaysia</option>
        <option>Penghu,Guangdong Province</option>
        <option>Perm,Russia</option>
        <option>Perth,Australia</option>
        <option>Peshawar,Pakistan</option>
        <option>Petropavlosk,Russia</option>
        <option>Philadelphia,Pennsylvania</option>
        <option>Philipsburg,ST. Maarten</option>
        <option>Phnom Penh,Cambodia</option>
        <option>Phoenix,United States</option>
        <option>Phuoc Long,Vietnam</option>
        <option>Pilar,Argentina</option>
        <option>Pinghai,Guangdong Province</option>
        <option>Pingzhou,Hunan Province</option>
        <option>Pipavav,India</option>
        <option>Piraeus,Greece</option>
        <option>Pisa,Italy</option>
        <option>Pittsburgh,Pennsylvania</option>
        <option>Ploce,Croatia</option>
        <option>Plymouth,Trinidad</option>
        <option>Podgorica,Montenegro</option>
        <option>Pohang,South Korea</option>
        <option>Pohnpei,Micronesia Islands</option>
        <option>Point A Pitre,Guadeloupe</option>
        <option>Point Lisas,Trinidad</option>
        <option>Pointe Blanche,Caribbean</option>
        <option>Pointe Des Galets,Reunion Islands</option>
        <option>Pointe Noire,Congo</option>
        <option>Pointe-A-Pitre,Leeward Island</option>
        <option>Pomezia,Italy</option>
        <option>Ponce,Puerto Rico</option>
        <option>Pontianak,Indonesia</option>
        <option>Pori,Finland</option>
        <option>Port Alma,Queensland</option>
        <option>Port Cabello,Venezuela</option>
        <option>Port Chalmers,New Zealand</option>
        <option>Port Des Galets,Africa</option>
        <option>Port Elizabeth,South Africa</option>
        <option>Port Everglades,Florida</option>
        <option>Port Gentil,Gabon</option>
        <option>Port Harcourt,Nigeria</option>
        <option>Port Hedland,Australia</option>
        <option>Port Kasim,Pakistan</option>
        <option>Port Kembla,Australia</option>
        <option>Port Klang,Malaysia</option>
        <option>Port Klang (North),Malaysia</option>
        <option>Port Klang (West),Malaysia</option>
        <option>Port Limon,Costa Rica</option>
        <option>Port Lisas,Panama</option>
        <option>Port Louis,Mauritius Is.</option>
        <option>Port Moresby,Papua New Guinea</option>
        <option>Port Muhammad Bin Qasim,India</option>
        <option>Port Noire,Congo</option>
        <option>Port of Spain,Trinidad</option>
        <option>Port Pirie,South Australia</option>
        <option>Port Qasim,Pakistan</option>
        <option>Port Rashid,United Arab Emirates</option>
        <option>Port Reunion,South Africa</option>
        <option>Port Said,Egypt</option>
        <option>Port Sousse,Tunisia</option>
        <option>Port Sudan,Sudan</option>
        <option>Port Suez,Egypt</option>
        <option>Port Sultan Qaboos,Oman</option>
        <option>Port Victoria,East Africa</option>
        <option>Port Vila,Vanuatu</option>
        <option>Port-Au-Prince,Haiti</option>
        <option>Portland,Oregon</option>
        <option>Porto,Portugal</option>
        <option>Porto Alegre,Brazil</option>
        <option>Portsmouth,Virginia</option>
        <option>Posorja,Ecuador</option>
        <option>Poti,Georgia</option>
        <option>Potianak,Indonesia</option>
        <option>Poznan,Poland</option>
        <option>Prague,Czech Republic</option>
        <option>Praia,Cape Varde</option>
        <option>Praia Mole,Brazil</option>
        <option>Prato (Inland Point),Italy</option>
        <option>Pretoria,Mozambique</option>
        <option>Prince Rupert,Canada</option>
        <option>Prishtina,Serbia</option>
        <option>Pristina,Kosovo</option>
        <option>Progreso,Mexico</option>
        <option>Providence,Kentucky</option>
        <option>Provinciales,Provinciales</option>
        <option>Pskov,Russia</option>
        <option>Pudong,Jiangsu Province</option>
        <option>Pudong,Shanghai</option>
        <option>Puerto Angamos,Peru</option>
        <option>Puerto Armuelles,Panama</option>
        <option>Puerto Bolivar,Colombia</option>
        <option>Puerto Cabello,Venezuela</option>
        <option>Puerto Caldera,Costa Rica</option>
        <option>Puerto Coronel,Chile</option>
        <option>Puerto Cortes,Honduras</option>
        <option>Puerto Limon,Costa Rica</option>
        <option>Puerto Madryn,Argentina</option>
        <option>Puerto Moin,United States</option>
        <option>Puerto Montt,Chile</option>
        <option>Puerto Morelos,Mexico</option>
        <option>Puerto Plata,Dominican Republic</option>
        <option>Puerto Quetzal (San Jose),Guatemala</option>
        <option>Puerto Sucre,Venezuela</option>
        <option>Puinhon,Vietnam</option>
        <option>Pune,India</option>
        <option>Puning,Guangdong Province</option>
        <option>Punta Arenas,Chile</option>
        <option>Puntarenas,Costa Rica</option>
        <option>Puqi,Zhejiang Province</option>
        <option>Putian,Fujian Province</option>
        <option>Pyeongtaek,South Korea</option>
        <option>Qesim Island,United Arab Emirates</option>
        <option>Qingdao,Shandong Province</option>
        <option>Qingpu,Shanghai</option>
        <option>Qingyuan,Guangdong Province</option>
        <option>Qinhuangdao,Hebei Province</option>
        <option>Qinzhou,Guangxi Province</option>
        <option>Quang Ninh,Vietnam</option>
        <option>Quanzhou,Fujian Province</option>
        <option>Quelimane,Mozambique</option>
        <option>Queretaro,Mexico</option>
        <option>Quertaro,Mexico</option>
        <option>Quezaltenango,Guatemala</option>
        <option>Quinhon,Vietnam</option>
        <option>Quito,Ecuador</option>
        <option>Quzai,Lebanon</option>
        <option>Quzhou,Zhejiang Province</option>
        <option>Rabaul,Papua New Guinea</option>
        <option>Radom,Poland</option>
        <option>Raleigh,North Carolina</option>
        <option>Rarotonga,Cook Islands</option>
        <option>Ras Al Khaimah,United Arab Emirates</option>
        <option>Ras Lanuf,Libya</option>
        <option>Rauma,Finland</option>
        <option>Ravenna,Italy</option>
        <option>Rayong,Thailand</option>
        <option>Recife,Brazil</option>
        <option>Regina,Italy</option>
        <option>Reunion,Reunion Islands</option>
        <option>Reykjavik,Iceland</option>
        <option>Richards Bay,South Africa</option>
        <option>Richmond,Virginia</option>
        <option>Ried,Austria</option>
        <option>Riga,Latvia</option>
        <option>Rijeka,Croatia</option>
        <option>Rio de Janeiro,Brazil</option>
        <option>Rio Grande,Brazil</option>
        <option>Rio Grande (A),Argentina</option>
        <option>Rio Grande Do Sul,Brazil</option>
        <option>Rio Haina,Dominican Republic</option>
        <option>Riyadh,Saudi Arabia</option>
        <option>Rizhao,Shandong Province</option>
        <option>Roadtown,Tortola</option>
        <option>Roanne,France</option>
        <option>Rochelle,United States</option>
        <option>Rodman,Panama</option>
        <option>Roenoe,Denmark</option>
        <option>Rome,Italy</option>
        <option>Rongqi,Guangdong Province</option>
        <option>Rosario,Argentina</option>
        <option>Rosarito,Mexico</option>
        <option>Roseau,Dominica</option>
        <option>Rostock,Germany</option>
        <option>Rostov,Georgia</option>
        <option>Rotorua,New Zealand</option>
        <option>Rotterdam,Netherlands</option>
        <option>Rouen,France</option>
        <option>Rovno,Russia</option>
        <option>Rudong,Jiangsu Province</option>
        <option>Ruian,Zhejiang Province</option>
        <option>Russe,Bulgaria</option>
        <option>Russia,Russia</option>
        <option>Rwanda,Africa</option>
        <option>Ryazanj,Russia</option>
        <option>Rzeszow,Poland</option>
        <option>S. Vicente,Cape Varde</option>
        <option>Sacramento,California</option>
        <option>Saint-Etienne,France</option>
        <option>Saipan,Marina Islands</option>
        <option>Sakaiminato,Japan</option>
        <option>Sakaisenboku,Japan</option>
        <option>Sakata,Japan</option>
        <option>Sakhalin,Russia</option>
        <option>Salalah,Oman</option>
        <option>Salerno,Italy</option>
        <option>Salina Cruz,Mexico</option>
        <option>Salomague,Philippines</option>
        <option>Salonica,Greece</option>
        <option>Salonika,Tanzania</option>
        <option>Salt Lake City,United States</option>
        <option>Salvador,Brazil</option>
        <option>Salzburg,Austria</option>
        <option>Samara,Russia</option>
        <option>Samarinda,Indonesia</option>
        <option>Samarkand,Russia</option>
        <option>Sambeimen,Guangdong Province</option>
        <option>Samsun,Turkey</option>
        <option>San Antonio,Chile</option>
        <option>San Antonio (TX),Texas</option>
        <option>San Diego,California</option>
        <option>San Felix,Chile</option>
        <option>San Francisco,California</option>
        <option>San Jose,Costa Rica</option>
        <option>San Juan,Puerto Rico</option>
        <option>San Lorenzo,Honduras</option>
        <option>San Luis Colorado,Colorado</option>
        <option>San Luis Potosi,Mexico</option>
        <option>San Pedro,Argentina</option>
        <option>San Pedro Sula,Honduras</option>
        <option>San Salvador,Republic of El Salvador</option>
        <option>San Vicente,Chile</option>
        <option>Sana,Yemen</option>
        <option>Sanbeimen,Guangdong Province</option>
        <option>Sanbu,Guangdong Province</option>
        <option>Sandakan, Sabah,Malaysia</option>
        <option>Sanrong,Guangdong Province</option>
        <option>Sanshan,Guangdong Province</option>
        <option>Sanshui,Guangdong Province</option>
        <option>Santa Cruz de Tenerife,Canary Islands</option>
        <option>Santa Marta,Colombia</option>
        <option>Santiago,Chile</option>
        <option>Santo,Vanuatu</option>
        <option>Santo Domingo,Dominican Republic</option>
        <option>Santo Tomas de Castilla,Guatemala</option>
        <option>Santos,Brazil</option>
        <option>Sanya,Hainan Province</option>
        <option>Sao Francisco Do Sul,Brazil</option>
        <option>Sao Paulo,Brazil</option>
        <option>Sao Tome,Western Africa</option>
        <option>Sarajevo,Bosnia Hercegovina</option>
        <option>Sarikei,Malaysia</option>
        <option>Saskatoon,Canada</option>
        <option>Savador Bahia,Brazil</option>
        <option>Savannah,Georgia</option>
        <option>Savannakhet,Laos</option>
        <option>Savona,Italy</option>
        <option>Savu Savu,Fiji Island</option>
        <option>Seattle,Washington</option>
        <option>Segoro,Indonesia</option>
        <option>Semarang,Indonesia</option>
        <option>Senboku,Japan</option>
        <option>Sendai,Japan</option>
        <option>Sens,France</option>
        <option>Seoul,South Korea</option>
        <option>Sepetiba,Brazil</option>
        <option>Sete,France</option>
        <option>Setubal,Portugal</option>
        <option>Seward,Alaska</option>
        <option>Sfax,Tunisia</option>
        <option>Shangchuan Dao,China</option>
        <option>Shangdong,Shandong Province</option>
        <option>Shanghai,China</option>
        <option>Shangqiu,Henan Province</option>
        <option>Shantou,Guangdong Province</option>
        <option>Shanwei,Guangdong Province</option>
        <option>Shaoguan,Guangdong Province</option>
        <option>Shaoxing,Zhejiang Province</option>
        <option>Sharjah,United Arab Emirates</option>
        <option>Shashi,Hubei Province</option>
        <option>Shatian,Guangdong Province</option>
        <option>Sheerness,U.K.</option>
        <option>Shekou,Guangdong Province</option>
        <option>Shenwan,Guangdong Province</option>
        <option>Shenyang,Liaoning Province</option>
        <option>Shenzhen,Guangdong Province</option>
        <option>Shibushi,Japan</option>
        <option>Shidao,Shandong Province</option>
        <option>Shijiazhuang,Hebei Province</option>
        <option>Shiliugang,Guangdong Province</option>
        <option>Shima,Japan</option>
        <option>Shimizu,Japan</option>
        <option>Shimonoseki,Japan</option>
        <option>Shiqi,Guangdong Province</option>
        <option>Shiqiao (Pan Yu),Guangdong Province</option>
        <option>Shishi,Fujian Province</option>
        <option>Shitang,Guangdong Province</option>
        <option>Shiwan,Guangdong Province</option>
        <option>Shuaibah,Kuwait</option>
        <option>Shuidong,Guangdong Province</option>
        <option>Shuikou,Guangdong Province</option>
        <option>Shunde,Guangdong Province</option>
        <option>Shuwaikh,Kuwait</option>
        <option>Sialkot,Pakistan</option>
        <option>Siam,Thailand</option>
        <option>Sibu, Sarawak,Malaysia</option>
        <option>Sichuan,Sichuan Province</option>
        <option>Sihanoukville,Cambodia</option>
        <option>Sihui,Guangdong Province</option>
        <option>Sines,Portugal</option>
        <option>Singapore,Singapore</option>
        <option>Sipitang,Malaysia</option>
        <option>Skikda,Algeria</option>
        <option>Skopje,Macedonia</option>
        <option>Smolensk,Russia</option>
        <option>Sochi,Russia</option>
        <option>Socola,Romania</option>
        <option>Sofia,Bulgaria</option>
        <option>Sohar,Oman</option>
        <option>Sokhna,Egypt</option>
        <option>Somalia,Africa</option>
        <option>Songkhla,Thailand</option>
        <option>Sousse,Tunisia</option>
        <option>South Caicos,Turks & Caicos</option>
        <option>South Shields,U.K.</option>
        <option>Southampton,U.K.</option>
        <option>Sovgavanj,Russia</option>
        <option>Soyo,Angola</option>
        <option>Sparrow Point,Maryland</option>
        <option>Split,Croatia</option>
        <option>Sri Racha (Bangkok),Thailand</option>
        <option>St. Barthelemy,Guadeloupe</option>
        <option>St. Croix,Virgin Islands</option>
        <option>St. Domingo,United States</option>
        <option>St. George's,Grenada</option>
        <option>St. Johns,Antigua</option>
        <option>St. Louis,Missouri</option>
        <option>St. Lucia,West Indies</option>
        <option>St. Maarten,Caribbean</option>
        <option>St. Petersburg,Russia</option>
        <option>St. Polten,Austria</option>
        <option>St. Thomas,Virgin Islands</option>
        <option>Stockholm,Sweden</option>
        <option>Stockton,California</option>
        <option>Stoughton,United States</option>
        <option>Stuttgart,Germany</option>
        <option>Su Wan Na Kaed,Vietnam</option>
        <option>Suape,Brazil</option>
        <option>Subic Bay,Philippines</option>
        <option>Suez Canal,Egypt</option>
        <option>Suigang,Hunan Province</option>
        <option>Sukhna,Egypt</option>
        <option>Surabaya,Indonesia</option>
        <option>Surat,India</option>
        <option>Surgut,Russia</option>
        <option>Suva,Fiji Island</option>
        <option>Suzhou,Jiangsu Province</option>
        <option>Svobodny,Russia</option>
        <option>Swaziland,Africa</option>
        <option>Sydney,Australia</option>
        <option>Szczecin,Poland</option>
        <option>Ta Kaek,Vietnam</option>
        <option>Ta Na Lang,Vietnam</option>
        <option>Tacoma,Washington</option>
        <option>Taicang,Jiangsu Province</option>
        <option>Taichung,China Taiwan</option>
        <option>Taijiang,Fujian Province</option>
        <option>Taipei,China Taiwan</option>
        <option>Taiping,Guangdong Province</option>
        <option>Taishan,Guangdong Province</option>
        <option>Taiwan,China Taiwan</option>
        <option>Taiyuan,Shanxi Province</option>
        <option>Taizhou,Zhejiang Province</option>
        <option>Takamatsu,Japan</option>
        <option>Takoradi,Ghana</option>
        <option>Talcahuano,Chile</option>
        <option>Taldykorgan,Kazakhstan</option>
        <option>Tallinn,Estonia</option>
        <option>Tamatave,Madagascar</option>
        <option>Tampa,Florida</option>
        <option>Tampere,Finland</option>
        <option>Tampico,Mexico</option>
        <option>Tancang,Vietnam</option>
        <option>Tanga,Tanzania</option>
        <option>Tanger-Med,Morocco</option>
        <option>Tanggu,Tianjin</option>
        <option>Tangier,Morocco</option>
        <option>Tangshan,Hebei Province</option>
        <option>Tanjung Emas,Indonesia</option>
        <option>Tanjung Manis,Malaysia</option>
        <option>Tanjung Pelepas,Malaysia</option>
        <option>Tao Yuan,China Taiwan</option>
        <option>Taranto,Italy</option>
        <option>Tarawa,Kirbati</option>
        <option>Tarnobrzeg,Poland</option>
        <option>Tarragona,Spain</option>
        <option>Tashkent,Uzbekistan</option>
        <option>Tauranga,New Zealand</option>
        <option>Tawau,Malaysia</option>
        <option>Tbilisi,Georgia</option>
        <option>Tcbuen,Colombia</option>
        <option>Tecate,Mexico</option>
        <option>Teesport,U.K.</option>
        <option>Tegucigalpa,Honduras</option>
        <option>Tekirdag,Turkey</option>
        <option>Tel Aviv,Israel</option>
        <option>Tema,Ghana</option>
        <option>Tenerife,Canary Islands</option>
        <option>Teplice,Czech Republic</option>
        <option>Tequcigalpa,Honduras</option>
        <option>Terespol,Poland</option>
        <option>Terport,Paraguay</option>
        <option>Thamesport,U.K.</option>
        <option>The Valley,Anguilla</option>
        <option>Thessaloniki,Greece</option>
        <option>Thilawa,Burma</option>
        <option>Tijuana,Mexico</option>
        <option>Tilbury,U.K.</option>
        <option>Timaru,New Zealand</option>
        <option>Tincan,Nigeria</option>
        <option>Tinian,Micronesia Islands</option>
        <option>Tirana,Albania</option>
        <option>Toamasina,Madagascar</option>
        <option>Tobata,Japan</option>
        <option>Tobruk,Africa</option>
        <option>Togliatti,Russia</option>
        <option>Tokmak,Kyrgyzstan</option>
        <option>Tokushima,Japan</option>
        <option>Tokuyama,Japan</option>
        <option>Tokyo,Japan</option>
        <option>Toljati,Russia</option>
        <option>Tomakomai,Japan</option>
        <option>Tomsk,Russia</option>
        <option>Tongan,Fujian Province</option>
        <option>Tonglin,Anhui Province</option>
        <option>Tonglu,Zhejiang Province</option>
        <option>Tongshen,Hubei Province</option>
        <option>Torghundi,Afghanistan</option>
        <option>Toronto,Ontario</option>
        <option>Torres Strait,Australia</option>
        <option>Torun,Poland</option>
        <option>Tosu,Japan</option>
        <option>Townsville,Australia</option>
        <option>Toyama,Japan</option>
        <option>Toyamashiniko,Japan</option>
        <option>Toyohashi,Japan</option>
        <option>Toytepa,Uzbekistan</option>
        <option>Trabzon,Turkey</option>
        <option>Trieste,Italy</option>
        <option>Trinidad,Caribbean</option>
        <option>Tripoli,Libya</option>
        <option>Trizt,Turkey</option>
        <option>Troyes,France</option>
        <option>Truk,Marina Islands</option>
        <option>Tsuruga,Japan</option>
        <option>Tulear,Madagascar</option>
        <option>Tumen,Jilin Province</option>
        <option>Tunis,Tunisia</option>
        <option>Turgundi,Russia</option>
        <option>Turku,Finland</option>
        <option>Tuticorin,India</option>
        <option>Tynda,Russia</option>
        <option>Tyumen,Russia</option>
        <option>Ube,Japan</option>
        <option>Ufa,Russia</option>
        <option>Ujung Pandang,Indonesia</option>
        <option>Ulaan Baatar,Mongolia</option>
        <option>Ulan Ude,Russia</option>
        <option>Uljanovsk,Russia</option>
        <option>Ulm,Germany</option>
        <option>Ulsan,South Korea</option>
        <option>Umm Qasr,Iraq</option>
        <option>Uralsk,Kazakhstan</option>
        <option>Urumqi,Xinjiang Province</option>
        <option>Ushuaia,Argentina</option>
        <option>Ussuryisk,Russia</option>
        <option>Ust-Kamenogorsk,Kazakhstan</option>
        <option>Vainikkala,Finland</option>
        <option>Valence,France</option>
        <option>Valencia,Spain</option>
        <option>Valletta,Malta</option>
        <option>Valparaiso,Chile</option>
        <option>Vancouver,British Columbia</option>
        <option>Vanino,Russia</option>
        <option>Varna,Bulgaria</option>
        <option>Vavau,Tonga</option>
        <option>Venezia,Italy</option>
        <option>Venice,Italy</option>
        <option>Vennica,Russia</option>
        <option>Vera Cruz,Mexico</option>
        <option>Verino,Russia</option>
        <option>Vernon,United States</option>
        <option>Vesoul,France</option>
        <option>Vict,Vietnam</option>
        <option>Victoria,Argentina</option>
        <option>Victoria (E.Africa),Seychelles</option>
        <option>Vienna,Austria</option>
        <option>Vientiane,Laos</option>
        <option>Vieux Fort,Guadeloupe</option>
        <option>Vigo,Spain</option>
        <option>Vila,Vanuatu</option>
        <option>Vila Do Conde,Brazil</option>
        <option>Villa Nueva,Honduras</option>
        <option>Vilnius,Lithuania</option>
        <option>Virgin Gorda,Caribbean</option>
        <option>Visakhapatnam,India</option>
        <option>Vitebsk,Russia</option>
        <option>Vitoria,Brazil</option>
        <option>Vizag,India</option>
        <option>Vladivostok,Russia</option>
        <option>Vohemar,Madagascar</option>
        <option>Volgogard,Russia</option>
        <option>Vologda,Russia</option>
        <option>Volos,Greece</option>
        <option>Voltri,Italy</option>
        <option>Voronez,Russia</option>
        <option>Vostochny,Russia</option>
        <option>Vungtau,Vietnam</option>
        <option>Wai Gao Qiao,Shanghai</option>
        <option>Wakayama,Japan</option>
        <option>Wallis/Futuna,Micronesia Islands</option>
        <option>Walvis Bay,Namiba</option>
        <option>Wanganui,New Zealand</option>
        <option>Wanzai (Zhuhai),Guangdong Province</option>
        <option>Warren,Ohio</option>
        <option>Warri,Nigeria</option>
        <option>Warsaw,Poland</option>
        <option>Wasilla,Alaska</option>
        <option>Weifang,Shandong Province</option>
        <option>Weihai,Shandong Province</option>
        <option>Weitou,Fujian Province</option>
        <option>Wellington,New Zealand</option>
        <option>Wenzhou,Zhejiang Province</option>
        <option>West Palm Beach,Florida</option>
        <option>Wewak,Papua New Guinea</option>
        <option>Whangarei,New Zealand</option>
        <option>Whitestown,United States</option>
        <option>Wilhelmshaven,Germany</option>
        <option>Willemstad,Netherlands Antilles</option>
        <option>Wilmington,North Carolina</option>
        <option>Winnipeg,Canada</option>
        <option>Wloclawek,Poland</option>
        <option>Wolow,Poland</option>
        <option>Wroclaw,Poland</option>
        <option>Wuchun,Guangdong Province</option>
        <option>Wuhan,Hubei Province</option>
        <option>Wuhu,Anhui Province</option>
        <option>Wujiang,Jiangsu Province</option>
        <option>Wulumuqi,Xinjiang Province</option>
        <option>Wumen,Zhejiang Province</option>
        <option>Wuxi,Jiangsu Province</option>
        <option>Wuzhou,Guangxi Province</option>
        <option>Xanshi,China</option>
        <option>Xiamen,Fujian Province</option>
        <option>Xian,Shaanxi Province</option>
        <option>Xiandria,China</option>
        <option>Xiangtan,Hunan Province</option>
        <option>Xiangyu,Xiamen</option>
        <option>Xiangzhou,Guangdong Province</option>
        <option>Xianyang,Shaanxi Province</option>
        <option>Xiao Cuo,Fujian Province</option>
        <option>Xiaogan,Hubei Province</option>
        <option>Xiaohudao,Guangdong Province</option>
        <option>Xiaolan (Shi Qi),Guangdong Province</option>
        <option>Xiaoshan,Zhejiang Province</option>
        <option>Xin Sha,Guangdong Province</option>
        <option>Xinfeng,Guangdong Province</option>
        <option>Xingang,Tianjin</option>
        <option>Xinhui,Guangdong Province</option>
        <option>Xining,Qinghai Province</option>
        <option>Xintang,Guangdong Province</option>
        <option>Xinyou,Fujian Province</option>
        <option>Xiuhui,Guangdong Province</option>
        <option>Xiuyu,Liaoning Province</option>
        <option>Xuchang,Henan Province</option>
        <option>Xuzhou,Jiangsu Province</option>
        <option>Yakusk,Russia</option>
        <option>Yangjiang,Guangdong Province</option>
        <option>Yangon,Burma</option>
        <option>Yangpu,Hainan Province</option>
        <option>Yangshan,Shanghai</option>
        <option>Yangzhou,Jiangsu Province</option>
        <option>Yantai,Shandong Province</option>
        <option>Yantian,Guangdong Province</option>
        <option>Yap,Micronesia Islands</option>
        <option>Yarimca,Turkey</option>
        <option>Yatsushiro,Japan</option>
        <option>Yawata,Japan</option>
        <option>Yckaterinburg,Russia</option>
        <option>Yeochon,South Korea</option>
        <option>Yeosu,South Korea</option>
        <option>Yeravan,Armenia</option>
        <option>Yi Chang,Hubei Province</option>
        <option>Yibin,Sichuan Province</option>
        <option>Yinchuan,Ningxia Province</option>
        <option>Yingkou,Liaoning Province</option>
        <option>Yiwu,Zhejiang Province</option>
        <option>Yixing,Jiangsu Province</option>
        <option>Yokkaichi,Japan</option>
        <option>Yokohama,Japan</option>
        <option>Yokosuka,Japan</option>
        <option>Yueyang,Hunan Province</option>
        <option>Yunfu,Guangdong Province</option>
        <option>Yunnan,Sichuan Province</option>
        <option>Yuyao,Zhejiang Province</option>
        <option>Zabaykalsk,Russia</option>
        <option>Zagreb,Croatia</option>
        <option>Zahony,Hungary</option>
        <option>Zambia,Africa</option>
        <option>Zamboanga,Philippines</option>
        <option>Zanzibar,Tanzania</option>
        <option>Zarate,Argentina</option>
        <option>Zarqa Free Zone,Jordan</option>
        <option>Zashita,Kazakhstan</option>
        <option>Zeebrugge,Belgium</option>
        <option>Zha Pu,Zhejiang Province</option>
        <option>Zhangjiagang,Jiangsu Province</option>
        <option>Zhangjiakou,Jiangsu Province</option>
        <option>Zhangzhou,Fujian Province</option>
        <option>Zhanjiang,Guangdong Province</option>
        <option>Zhaogang,China</option>
        <option>Zhaoqing,Guangdong Province</option>
        <option>Zhaoqing New Port,Guangdong Province</option>
        <option>Zhengzhou,Henan Province</option>
        <option>Zhenjiang,Jiangsu Province</option>
        <option>Zhenping,Henan Province</option>
        <option>Zhezkazgan,Kazakhstan</option>
        <option>Zhizhudao,Guangdong Province</option>
        <option>Zhongshan,Guangdong Province</option>
        <option>Zhongxinzhou,Guangdong Province</option>
        <option>Zhoushan,Zhejiang Province</option>
        <option>Zhoutouzui,Guangdong Province</option>
        <option>Zhuhai,Guangdong Province</option>
        <option>Zhuhai Port (Gaolan),Guangdong Province</option>
        <option>Zhuzhou,Hunan Province</option>
        <option>Zibo,Shandong Province</option>
        <option>Zimbabwe,Africa</option>
        <option>Zlin,Belgium</option>
        <option>Zurich,Switzerland</option>
            </datalist>
            <input  autoComplete="on" list="suggestions"/> 
        </div>
        <body>
            <label for="Select Delivery Point"><h2>Select Delivery Point</h2></label>
            <select name="Select Delivery Point" id="Select Delivery Point" required>
              <option value="CFS">CFS</option>
              <option value="FACTORY">FACTORY</option>
              <option value="ICD">ICD</option>
              <option value="PORT">PORT</option>
            </select>
          </body>
            <body>
              <form action="/action_page.php">
                <label for="Pickup time"><h2>DISPATCH (date and time)</h2></label>
                <input type="datetime-local" id="Pickup time" name="Pickup time" required>
              </form>
              </body>
                  <h1><B><I>CARGO DETAILS</I></B></h1>
                    <body>
                      <h2>Select CONTAINER TYPE</h2>
                      <select name="container type" id="container type" required>
                        <option value="STANDARD 20'">STANDARD 20'</option>
                        <option value="STANDARD 40'">STANDARD 40'</option>
                        <option value="REEFER 20'">REEFER 20'</option>
                        <option value="REFFER 40'">REFFER 40'</option>
                        <option value="REEFER 40' High Cube">REEFER 40' High Cube</option>
                        <option value="OPEN TOP 20'">OPEN TOP 20'</option>
                        <option value="OPEN TOP 40'">OPEN TOP 40'</option>
                        <option value="FLAT RACK 20'">FLAT RACK 20'</option>
                        <option value="FLAT RACK 40'">FLAT RACK 40'</option>
                        <option value="FLAT RACK 20' COLLAPSIBLE">FLAT RACK 20' COLLAPSIBLE</option>
                        <option value="FLAT RACK 40' COLLAPSIBLE">FLAT RACK 40' COLLAPSIBLE</option>
                        <option value="PLATFORM 20'">PLATFORM 20'</option>
                        <option value="PLATFORM 40'">PLATFORM 40'</option>
                        <option value="OTHER">OTHER</option>
                      </select>
                    </body>     
                    <body>
                  <form action="/action_page.php">
                    <label for="quantity">Select QTY</label>
                    <input type="number" id="quantity" name="quantity" min="1" max="999" required>
                  </form>
                  </body>
                  <body>
                      <h2>Gross Weight/CONTAINER</h2>
                      <form action="/action_page.php">
                        <label for="quantity"></label>
                        <input type="number" id="quantity" name="quantity" min="1" max="999999" required>
                      </form>
                      </body>
                      <body>
                          <label for="UNIT">Measure Unit</label>
                              <select name="measure unit" id="measure unit" required>
                              <option value=MT>MT</option>
                              <option value=KG>KG</option>
                          </select>
                      </body>                   
                          <body>
                          <div class="container">
                            <h2>Select Kind Of CARGO</h2>
                            <form>
                              <label class="radio-inline">
                                <input type="radio" name="optradio" >HAZARDOUS
                              </label>
                              <label class="radio-inline">
                                <input type="radio" name="optradio" checked>NON-HAZARDOUS
                              </label>
                            </form>
                          </div>
                          </body>
                          <body>
                      <h2>CLASSIFICATION(only if HAZ)</h2>
                      <select name="container type" id="container type">
                        <option value="2.1 Flammable gases">2.1 Flammable gases</option>
                        <option value="2.2 Non-Flammable Non-Toxic gases">2.2 Non-Flammable Non-Toxic gases</option>
                        <option value="2.3 Toxic gases">2.3 Toxic gases</option>
                        <option value="3 Inflammable Liquids">3 Inflammable Liquids</option>
                        <option value="4.1 Flammable Solids">4.1 Flammable Solids</option>
                        <option value="4.2 Substance liable to spontaneous combustion">4.2 Substance liable to spontaneous combustion</option>
                        <option value="4.3 Substance which in contact with water,emit Flammable gases">4.3 Substance which in contact with water,emit Flammable gases</option>
                        <option value="6.1 Toxic Substances">"6.1 Toxic Substances</option>
                        <option value="6.2 Infectious Substances">6.2 Infectious Substances</option>
                        <option value="7 Radioactive Substances">7 Radioactive Substances</option>
                        <option value="8 Corrosive Substances">8 Corrosive Substances</option>
                        <option value="9 Miscellaneous Dangerous Goods">9 Miscellaneous Dangerous Goods</option>
                      </select>
                  </body>     
                  <body>
                      <form action="/action_page.php">
                        <label for="UN no.">UN no.(only if HAZ)</label>
                        <input type="number" id="quantity" name="quantity" min="1" max="9999">
                      </form>
                      </body>
     <button type="submit">Send</button>
</form>
</html>
"""    
left_column, right_column = st.columns(2)  
with left_column:
 st.markdown(contact_form, unsafe_allow_html=True )
with right_column:
    st.empty()