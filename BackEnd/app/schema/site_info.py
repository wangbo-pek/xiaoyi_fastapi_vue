"""
    path: xiaoyi/BackEnd/schema/site_info.py
    description: 博客网站信息的Pydantic模型
"""
from datetime import datetime
from pydantic import BaseModel, Field


class SiteInfoOut(BaseModel):
    site_name: str = Field(..., description='网站名称', alias='siteName')
    site_subtitle: str = Field(..., description='网站名称网站副标题', alias='siteSubtitle')
    logo_url: str = Field(..., description='Logo地址', alias='logoUrl')
    favicon_url: str = Field(..., description='Favicon图标地址', alias='faviconUrl')
    icp_number: str = Field(..., description='ICP备案号', alias='icpNumber')
    public_security: str = Field(..., description='公网安备案号', alias='publicSecurity')
    github_url: str = Field(..., description='GitHub地址', alias='githubUrl')
    keywords: str = Field(..., description='SEO关键词')
    description: str = Field(..., description='SEO描述')
    created_time: datetime = Field(..., description="创建时间", alias='createdTime')
    updated_time: datetime = Field(..., description="更新时间", alias='updatedTime')
    wechat_sponsor_qr: str = Field(..., description='微信收款二维码地址', alias='wechatSponsorQR')
    alipay_sponsor_qr: str = Field(..., description='支付宝收款二维码地址', alias='alipaySponsorQR')

    class Config:
        from_attributes = True
        validate_by_name = True
