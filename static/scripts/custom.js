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

    })

})