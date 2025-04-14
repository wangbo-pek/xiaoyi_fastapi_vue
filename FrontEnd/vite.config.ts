import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import vuetify from "vite-plugin-vuetify";
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        vuetify()
    ],
    resolve:{
        alias:{
            '@':path.resolve(__dirname, 'src')
        }
    },
    css: {
        preprocessorOptions: {
            scss: {
                // 自动引入
                additionalData: `
                @use "@/styles/variables.scss";
                @use "@/styles/mixins.scss";
                `
            }
        }
    }
})
