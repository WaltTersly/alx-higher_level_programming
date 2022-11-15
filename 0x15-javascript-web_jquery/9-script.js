$.get("https://fourtonfish.com/hellosalut/?lang=fr", data,
    function (data, textStatus) {
        if (textStatus === 'success') {
            $('#hello').text(data.hello);
        }
    },
);