from IPython.display import display, HTML
display(HTML("""
<button type="button" id="button_for_indexeddb">Click This Button Before Typing Anything</button>
<script>
window.button_for_indexeddb.onclick = function(e) {
    // Change the button text to "Local Environment Successfully Updated!" after it is clicked
    e.target.innerText = "Local Environment Successfully Updated!";
    
    window.indexedDB.open('JupyterLite Storage').onsuccess = function(e) {
        let tables = ["checkpoints", "files"];
        let db = e.target.result;
        let t = db.transaction(tables, "readwrite");

        function clearTable(tablename) {
            let st = t.objectStore(tablename);
            st.count().onsuccess = function(e) {
                console.log("Deleting " + e.target.result + " entries from " + tablename + "...");
                st.clear().onsuccess = function(e) {
                    console.log(tablename + " is cleared!");
                }
            }
        }

        for (let tablename of tables) {
            clearTable(tablename);
        }
    }
};
</script>
"""))
