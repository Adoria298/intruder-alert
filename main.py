def bluetooth_launch():
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.SQUARE)
bluetooth.on_bluetooth_connected(bluetooth_launch)

bluetooth.start_accelerometer_service()
bluetooth.start_button_service()