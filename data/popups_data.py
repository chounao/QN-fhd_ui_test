# coding=utf-8


class PopupswindowsPageData:
    """
    广告公告和风火券
    """
    #公告id
    announcement_selectors = ['id','systemNotice']
    #公告关闭按钮
    close_Abtn_selectors = ['id','systemNoticeConfirm']

    #弹窗 付费弹窗：双11活动，风火券
    Pay_popup_selectors = ['class','ant-modal-root']
    #关闭按钮
    close_btn_selectors = ['class','ant-modal-close-x']