// this makes all of the "topics" into collapsible sections

// collapses or un-collapses the specified object
function toggle_collapse(target){
    if(target.style.display === "none"){
        target.style.display = "block";
    }else{
        target.style.display = "none";
    }
}

// collapses or un-collapses the object with the target id
function toggle_collapse_id(target_id){
    toggle_collapse(document.getElementById(target_id));
}