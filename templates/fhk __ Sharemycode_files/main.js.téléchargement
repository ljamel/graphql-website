// Global variables
let editorInstance, userIsAdmin;
let remoteCodeInfos = { timestamp: 0, size: 0 };
let storage = new CodeStorage; // 'user', 'sharecodes' in localStorage

// When DOM is loaded
$(function () {
  switch (storage.user.preferences.theme) {
    case 'vscode-dark':
    case 'monokai-sublime':
      document.querySelector('div.actionbar').style.background = 'rgb(15, 17, 26)';
      break;
    case 'mdn-like':
      document.querySelector('div.actionbar').style.background = '#fff';
      break;
    default:
      document.querySelector('div.actionbar').style.background = ' #20242f';
  }
  // ajouter l'attribute selected sur l'option choisie dans le select
  for (let option of document.querySelectorAll('select#theme option')) {
    option.removeAttribute('selected');
    if (storage.user.preferences.theme === option.value) {
      option.selected = true
    }
  }
  // Let's launch the loop (checking remote code each 0.5 seconds)
  checkCode();
});
