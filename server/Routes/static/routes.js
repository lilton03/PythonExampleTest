    function page_load() {
    $.getJSON($SCRIPT_ROOT+'/_get_page_data',{},
        function (data) {
        console.log(data)
    })
}


