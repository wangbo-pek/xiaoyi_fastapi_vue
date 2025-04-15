export const routesArray = [
    {
        path: 'home',
        name: 'home',
        component: () => import('@/views/blog/home/Home.vue'),
        meta: {
            title: '首页'
        }
    },
    {
        path: 'note',
        name: 'note',
        component: () => import('@/views/blog/note/Note.vue'),
        meta: {
            title: "笔记"
        }
    },
    {
        path: 'diary',
        name: 'diary',
        component: () => import('@/views/blog/diary/Diary.vue'),
        meta: {
            title: "日记"
        }
    },
    {
        path: 'tags',
        name: 'tags',
        component: () => import('@/views/blog/tag/Tag.vue'),
        meta: {
            title: "标签"
        }
    },
]