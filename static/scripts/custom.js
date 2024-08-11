$(document).ready(function(){
    // add to selectionss

    $('.add-to-selection').on("click",function(){
        let button = $(this)
        let id = button.attr('data-index')
    

        let hotel_id=$('#id').val()
        let room_id=$(`.room_id_${id}`).val()
        let room_number=$(`.room_number_${id}`).val()
        let hotel_name=$('#hotel_name').val()
        let room_name=$("#room_name").val()
        let room_price=$("#room_price").val()
        let number_of_beds=$("#number_of_beds").val()
        let room_type=$("#room_type").val()
        let checkin=$("#checkin").val()
        let checkout=$("#checkout").val()
        let adult=$("#adult").val()
        let children=$("#children").val()





        console.log(hotel_id)
        console.log(room_id)
        console.log(room_number)
        console.log(hotel_name)
        console.log(room_name)
        console.log(room_price)
        console.log(number_of_beds)
        console.log(room_type)
        console.log(checkin)
        console.log(checkout)
        console.log(adult)
        console.log(children)

        $.ajax({
            url:'/booking/add_to_selection',
            data:{
                'id':id,
                'hotel_id':hotel_id,
                'room_id':room_id,
                'room_number':room_number,
                'hotel_name':hotel_name,
                'room_name':room_name,
                'room_type':room_type,
                'room_price':room_price,
                'number_of_beds':number_of_beds,
                'checkin':checkin,
                'checkout':checkout,
                'adult':adult,
                'children':children,

            },
            dataType: "json",
            beforeSend:function(){
                console.log("sending data to server")
            },
            success: function(response){
                console.log(response)
            }
        

        })

    })

})


// Delete Items From Cart

$(document).on("click", ".delete-item", function(){
    console.log('delected')
    let id = $(this).attr("data-item")
    console.log(id)
    let button = $(this)

    $.ajax({
        url: "/booking/delete_selection/",
        data:{
            'id':id

        },
        dataType: "json",
        beforeSend:function(){
            button.html(`<div class="spinner-border" role="status">
  <span class="sr-only">Loading...</span>
</div>`)
        },
        success:function(res){
            console.log(res)
        }
    })
})



function makeAjaxCall(){
    $.ajax({
        url:"/update_room_status/",
        type: "GET",
        success: function(data){
            console.log("checked Rooms")
        },
        
    })
}

setInterval(makeAjaxCall, 3000)