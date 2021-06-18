/**
 * Gets the code via Ajax (loaded in PHP from a text file)
 *
 * @todo   Get rid of jQuery for optimization sake
 * 
 * @param  {boolean} firstTime TRUE if this is the first loading of the function, FALSE if not
 * 
 * @return {void}
 */
function getCode(callback)
{
  // Ajax call to get the remote code
  $.get(
    "ajax/code_get.php?slug=" + urlSlug,
    function(data)
    {
      // We store the scrollTop position before reloading the code
      var scrollTop = editorInstance.getScrollInfo().top;

      // We update the local code within CodeMirror textarea (the scrollTop is thus re-initialized to 0)
      editorInstance.setValue(data.code);

      // If callback function is set
      callback();
      
      // We scroll the view back to its previous position
      editorInstance.scrollTo(0, scrollTop);

      // If user is not the admin, we re-launch the loop (to check remote code each 0.5 seconds)
      if (!userIsAdmin) checkCode();
    }
  );
}
