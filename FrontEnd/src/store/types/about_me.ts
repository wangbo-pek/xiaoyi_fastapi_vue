export interface MyDetail {
    "name": string,
    "nickname": string,
    "avatar": string,
    "motto": string,
    "email": string,
    "wechat": string,
    "wechatQR": string,
    "city": string,
    "shortIntro": string,
    "fullIntro": string,
    "wisdom": string,
}

export interface MyAbilityAndMySkill {
    "title": string,
    "description": string,
    "degree": number
}

export interface MyTask {
    "title": string,
    "status": number,
    "description": string,
    "progress": number,
    "priority": number,
    "isArchived": boolean,
    "createdTime": string,
}

export interface MyFavoriteLink {
    "title": string,
    "url": string,
    "faviconUrl": string,
    "isOutOfWall": boolean,
}
