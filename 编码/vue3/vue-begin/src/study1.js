import { createApp } from 'vue'
import App from './Page1.vue'

// import './assets/main.css'

 const app={
        data(){
            return {
                count:123,
                title: "你好"
            }
        }

    }

createApp(App).mount('#app')
// createApp(App).mount('#bpp')
