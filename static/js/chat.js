let input_message = $('#input-message');
let message_body = $('.msg-card-body');
let send_message_form = $('#send-message-form');
const USERNAME = $('#logged-in-user').val();

let loc = window.location;
let ws_start = "ws://";
if (loc.protocol === "https:") {
    ws_start = "wss://";
}
let endpoint = ws_start + loc.host + loc.pathname


var socket = new WebSocket(endpoint);

socket.onopen = async function (e) {
    console.log("open", e);

    send_message_form.on('submit', function (e){
        e.preventDefault()
        let message = input_message.val()
        let send_to = get_active_other_username()
        let thread_id = get_active_thread_id()

        let data = {
            'message': message,
            'sent_by': USERNAME,
            'send_to': send_to,
            'thread_id': thread_id
        }
        data = JSON.stringify(data)
        socket.send(data)
        $(this)[0].reset()
    });
}

socket.onmessage = async function (e) {
    console.log("message", e);

    let data = JSON.parse(e.data);
    let message = data["message"];
    let sent_by_username = data["sent_by"];
    let thread_id = data["thread_id"];

    new_message(message, sent_by_username, thread_id);
}

socket.onerror = async function (e) {
    console.log("error", e);
}

socket.onclose = async function (e) {
    console.log("close", e);
}

function new_message(message, sent_by_username, thread_id) {
    if ($.trim(message) === "") {
        return false;
    }

    let message_element;
    let chat_id = "chat_" + thread_id;

    if (sent_by_username === USERNAME) {
        message_element = `
			<div class="d-flex mb-4 replied">
				<div class="msg_cotainer_send">
					${message}
					<span class="msg_time_send">

                    </span>
				</div>
				<div class="img_cont_msg">

                </div>
			</div>
        `
    }
    else {
        message_element = `
            <div class="d-flex mb-4 received">
                <div class="img_cont_msg">

                </div>
                <div class="msg_cotainer">
                    ${message}
                    <span class="msg_time">
                    
                    </span>
                </div>
            </div>
        `
    }

    let message_body = $('.messages-wrapper[chat-id="' + chat_id + '"] .msg_card_body');
    message_body.append($(message_element));
    message_body.animate({scrollBottom: $(document).height()}, 100);

    input_message.val(null);
}

$(".contact-li").on("click", function() {
    $('.contacts .active').removeClass("active");
    $(this).addClass("active");

    let chat_id = $(this).attr("chat-id");
    $('.messages-wrapper.is_active').removeClass("is_active");
    $('.messages-wrapper[chat-id="' + chat_id +'"]').addClass("is_active");
})

function get_active_other_username() {
    let other_username = $('.messages-wrapper.is_active').attr("other-user-username");
    other_username = $.trim(other_username);

    return other_username;
}

function get_active_thread_id() {
    let chat_id = $('.messages-wrapper.is_active').attr("chat-id");
    let thread_id = chat_id.replace('chat_', '');

    return thread_id;
}
