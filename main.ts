bluetooth.onBluetoothConnected(function bluetooth_launch() {
    basic.showIcon(IconNames.SmallDiamond)
    basic.showIcon(IconNames.Diamond)
    basic.showIcon(IconNames.Square)
})
bluetooth.startAccelerometerService()
bluetooth.startButtonService()
