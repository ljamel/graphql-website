let tabElts = document.querySelectorAll('.tab');

function showContentTab() {
 for (let tab of tabElts) {
  tab.classList.remove('selected');
 }
 this.classList.add('selected');

 let sectionsElts = document.querySelectorAll('.tabsection');
 for (let section of sectionsElts) {
  section.classList.remove('selected');
 }
 if (this.classList.contains('notes')) {
  document.querySelector('.NotesSection').classList.add('selected');
 }
 if (this.classList.contains('playlist')) {
  document.querySelector('.CodelistSection').classList.add('selected');
 }
 if (this.classList.contains('about')) {
  document.querySelector('.AboutSection').classList.add('selected');
 }
 if (this.classList.contains('settings')) {
  document.querySelector('.SettingsSection').classList.add('selected');
 }
}

function chooseTheme() {
 // changer l'éditeur
 editorInstance.setOption('theme', this.value);
 // changer le backgound de l'action bar
 let bkg = window.getComputedStyle(document.querySelector(".CodeMirror ")).getPropertyValue('background');
 document.querySelector('div.actionbar').style.background = bkg;
 document.querySelector('select#langage').style.background = bkg;
 // setPreferences dans le localStorage
 storage.user.setPreferences({
  theme: this.value,
  fontsize: storage.user.preferences.fontsize
 });
}

function chooseFontSize(ev) {
 document.querySelector('.CodeMirror').style.fontSize = ev.target.value;
 storage.user.setPreferences({
  theme: storage.user.preferences.theme,
  fontsize: ev.target.value
 });
}

function changeLangage(ev) {
 editorInstance.setOption("mode", ev.target.value);
}

function openCloseSidebar() {
 if (this.classList.contains('open')) {
  document.querySelector('div.sidebarRight').style.transform = 'translateX(250px)';
  document.querySelector('div.sidebarRight').style.width = '0px';
  document.querySelector('div.sidebarRight').style.opacity = '0';
  //document.querySelector('div.actionbar').style.transform = 'translateX(250px)';
  this.classList.remove('open');
  this.classList.add('close');
 }
 else {
  document.querySelector('div.sidebarRight').style.transform = 'translateX(0px)';
  document.querySelector('div.sidebarRight').style.width = '410px';
  document.querySelector('div.sidebarRight').style.opacity = '1';
  //document.querySelector('div.actionbar').style.transform = 'translateX(0px)';
  this.classList.remove('close');
  this.classList.add('open');
 }
}


for (let tab of tabElts) {
 tab.addEventListener('click', showContentTab)
}

document.querySelector('select#theme').addEventListener('change', chooseTheme);
document.querySelector('select#selectfontsize').addEventListener('change', chooseFontSize);
document.querySelector('select#langage').addEventListener('change', changeLangage);


document.querySelector('button.openclosesidebar-icon').addEventListener('click', openCloseSidebar);

