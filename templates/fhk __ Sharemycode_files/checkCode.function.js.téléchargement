/**
 * Checks if remote code is different from local one
 *
 * @todo   Instead of comparing stored characteristics with remote ones,
 *         we should use a safer comparison system (string comparison ? commits ID ?)
 *         since fast typing don't give enough time
 *         for the AJAX calls & Code Mirror update to correctly be executed
 *         while stored characteristics will always be executed
 * 
 * @return {void}
 */
function checkCode() {
  $.get(
    "ajax/code_check.php?slug=" + urlSlug,
    function (data, textStatus, jqXHR) {
      // If this is the first loading (= Code Mirror is not attached yet)
      if (editorInstance === undefined) {
        // If HTTP status code is 201 (because this user is the first to use this slug, thus the code file has just been created),
        // we set the global variable userIsAdmin to TRUE (else FALSE)
        userIsAdmin = (jqXHR.status == 201) ? true : false;

        // We load Code Mirror
        loadCodeMirror();
      }

      // If remote code file characteristics are different from the stored ones
      // (we have to stringify objects to be able to compare them)
      // @see http://stackoverflow.com/questions/1068834/object-comparison-in-javascript
      if (JSON.stringify(data) != JSON.stringify(remoteCodeInfos)) {
        getCode(function () { remoteCodeInfos = data; console.log(remoteCodeInfos); });
      }
      else {
        // We check again potential new code in 0.5 seconds
        window.setTimeout(checkCode, 620);
      }
    }
  );
}
