$(document).ready(function () {
    var url = window.location.href;
    var params = url.split('/');
    var id = params[params.length - 1]
    $('#final_msg').hide()
    LoadProducts(id)

});


function LoadProducts(id) {
    $.ajax({
        url: "/stockapi/adminproducts/" + id,
        type: 'GET',

        success: function (response) {
            $('#imageone').attr("src", response.image.original)
            $('#productname').val(response.name)
            $('#productorder').val(response.order)

            $('#productpriceEuro').val(response.productpriceEuro)
            $('#OfferEuro').val(response.OfferEuro)

            $('#productpriceSterling').val(response.productpriceSterling)
            $('#OfferSterling').val(response.OfferSterling)

            $('#productpriceDollar').val(response.productpriceDollar)
            $('#OfferDollar').val(response.OfferDollar)

            $('#productpriceDirham').val(response.productpriceDirham)
            $('#OfferDirham').val(response.OfferDirham)

            $('#productpriceSar').val(response.productpriceSar)
            $('#OfferSAR').val(response.OfferSAR)

            $('#productID').val(response.id)
            $('#subsubcatID').val(response.subsubcategory)
            $('#nummberofproducts').html(response.options.length)
            for (let i = 0; i < response.options.length; i++) {
                $('#productrows').append(
                    `
                        <tr>
                        <td>`+ response.options[i].id + `</td>
                        <td>`+ response.options[i].color + `</td>
                        <td>Published</td>
                        </tr>
                        `
                )
            }
        },
        error: function (jqXHR) {
            console.log(JSON.stringify(jqXHR))
        }

    });

}

$('#editproduct').submit(function (event) {
    event.preventDefault()
    var csrf_token1 = $('[name="csrfmiddlewaretoken"]').val();
    var formData = new FormData(document.getElementById("editproduct"));
    formData.append("name", $("#productname").val());
    formData.append("order", $("#productorder").val());
    formData.append("productpriceEuro", $("#productpriceEuro").val());
    formData.append("productpriceSterling", $("#productpriceSterling").val());
    formData.append("productpriceDollar", $("#productpriceDollar").val());
    formData.append("productpriceDirham", $("#productpriceDirham").val());
    formData.append("productpriceSar", $("#productpriceSar").val());
    formData.append("subsubcategory", $("#subsubcatID").val());
    if (document.getElementById("dropify-event").files.length != 0) {
        formData.append("image", $("#dropify-event")[0].files[0]);
    }
    formData.append("csrfmiddlewaretoken", csrf_token1);
    data = formData
    id = $('#productID').val()
    $.ajax({
        url: "/stockapi/adminproducts/" + id + "/",
        type: 'PATCH',
        data: formData,
        processData: false,
        contentType: false,

        success: function (response) {
            
            if(response.offerID!=0){
                var data={
                    "OfferEuro":$("#OfferEuro").val(),
                    "OfferDollar":$("#OfferDollar").val(),
                    "OfferDirham":$("#OfferDirham").val(),
                    "OfferSterling":$("#OfferSterling").val(),
                    "OfferSAR":$("#OfferSAR").val(),
                }
                $.ajax({
                    url: "/stockapi/addoffers/" + response.offerID + "/",
                    type: 'PATCH',
                    dataType: "JSON",
                    data: data,
            
                    success: function (response) {

                    },
                });
            }
            else{
                data={
                    "OfferEuro":$("#productpriceEuro").val(),
                    "OfferDollar":$("#OfferDollar").val(),
                    "OfferDirham":$("#OfferDirham").val(),
                    "OfferSAR":$("#OfferSAR").val(),
                    "OfferSAR":$("#OfferSAR").val(),
                    "product":response.id,
                }
                $.ajax({
                    url: "/stockapi/addoffers/",
                    type: 'POST',
                    data: data,
                    dataType: 'JSON',

                    success: function (response) {
                        $('#productform').get(0).reset()
                        $('#final_msg').fadeIn().delay(1000).fadeOut();
                        $("img").attr("src", "https://dummyimage.com/150x200.gif")
                        Loadproducts()
                    },
                    error: function (jqXHR) {
                        console.log(jqXHR.responseText)
                    }

                });
            }
            $('#editproduct').get(0).reset()
                $('#final_msg').fadeIn().delay(1000).fadeOut();
            $("img").attr("src", "https://dummyimage.com/150x200.gif")
            LoadProducts(id)
        },
        error: function (jqXHR) {
            console.log(JSON.stringify(jqXHR.responseText))
        }

    });
});

$("#dropify-event").change(function () {
    $('#submitbutton').show()
    if (this.files && this.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#imageone').attr('src', e.target.result);
        }
        reader.readAsDataURL(this.files[0]);
    }
});
