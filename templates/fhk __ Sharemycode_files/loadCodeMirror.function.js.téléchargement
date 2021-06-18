/**
 * Loads Code Mirror and attaches it to #code textarea
 * 
 * @return {void}
 */
async function loadCodeMirror() {
  editorInstance = await CodeMirror.fromTextArea(
    document.getElementById('code'),
    {
      autofocus: userIsAdmin,
      tabSize: 4,
      indentUnit: 4,
      indentWithTabs: false,
      lineNumbers: true,
      lineWrapping: true,
      matchBrackets: true,
      mode: "application/x-httpd-php",
      readOnly: !userIsAdmin,
      smartIndent: false,
      theme: storage.user.preferences.theme,
      scrollbarStyle: null,
      autoCloseBrackets: true,
      autoCloseTags: true
    }
  );

  document.querySelector('.CodeMirror').style.fontSize = storage.user.preferences.fontsize;
  // ajouter l'attribute selected sur l'option choisie dans le select
  for (let option of document.querySelectorAll('select#selectfontsize option')) {
    option.removeAttribute('selected');
    if (storage.user.preferences.fontsize === option.value) {
      option.selected = true
    }
  }

  // If the user is the administrator, we install the 'change' event handler on the CodeMirror instance
  if (userIsAdmin) editorInstance.on('change', updateCode);

  // We install the 'keyup' event handler on the document to unfocus when "escape" key is pressed
  $(document).keyup(function (event) { if (event.keyCode == 27) editorInstance.getInputField().blur(); });
}
