import usb.core

class USBInfo():
    def __init__(self):
        self.interfaceClass = 8
    def __call__(self, device):
        if device.bDeviceClass == self.interfaceClass:
            return True
        for cfg in device:
            intf = usb.util.find_descriptor(
                cfg,
                bInterfaceClass=self.interfaceClass
            )
            if intf is not None:
                return True
        return False
    def filterUSBInfo(self, usbDict, label):
        usbInfo = {}
        for el in dir(usbDict):
            val = getattr(usbDict, el)
            if "__" not in el and el != "address" and (type(val) is str or type(val) is int):
                usbInfo[label+el] = val

        return usbInfo

    def getUSBInfo(self):
        usbs = usb.core.find(find_all=1, custom_match=USBInfo())
        usbInfoList = []
        for cfg in usbs:
            usbInfo = {}
            usbInfo.update(self.filterUSBInfo(cfg, "1. "))
            for intf in cfg:
                usbInfo.update(self.filterUSBInfo(intf, "2. "))
                for ep in intf:
                    usbInfo.update(self.filterUSBInfo(ep, "3. "))
                    for end in ep:
                        usbInfo.update(self.filterUSBInfo(end, "4. "))
            usbInfoList.append(usbInfo)

        usbNameList = []
        for i, usbVal in enumerate(usbInfoList):
            usbNameList.append(str(i) + ": [" + usbVal["1. manufacturer"] + ", " + usbVal["1. product"] + "]\n")

        if len(usbNameList) == 0:
            print("shoud be insert USB.")
            exit(1)
        print(''.join(usbNameList))
        usbType = input("keyUSB: ")

        try:
            int(usbType)
        except ValueError:
            print("shoud be input correct usbType.")
            exit(1)

        if int(usbType) >= len(usbNameList):
            print("shoud be input correct usbType.")
            exit(1)
        print()
        usbInfoStr = ""
        for key in usbInfoList[int(usbType)]:
            usbInfoStr+= "|" + str(usbInfoList[int(usbType)][key])
        return usbInfoStr + "|"


