<template>
  <div class="index">
    <div class="alert alert-primary">
      <strong>The service allows you to generate short links for important resources.</strong>
      <p class="mb-0">
        To create a short link, simply enter the resource in the input field below.
        A couple of seconds and you're done!
      </p>
    </div>

    <div class="card mb-3">
      <div class="card-body">
        <div class="row align-items-center">
          <div class="col-auto">
            <button class="btn btn-icon disabled">
              <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-forms" width="24" height="24"
                viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M12 3a3 3 0 0 0 -3 3v12a3 3 0 0 0 3 3"></path>
                <path d="M6 3a3 3 0 0 1 3 3v12a3 3 0 0 1 -3 3"></path>
                <path d="M13 7h7a1 1 0 0 1 1 1v8a1 1 0 0 1 -1 1h-7"></path>
                <path d="M5 7h-1a1 1 0 0 0 -1 1v8a1 1 0 0 0 1 1h1"></path>
                <path d="M17 12h.01"></path>
                <path d="M13 12h.01"></path>
              </svg>
            </button>
          </div>
          <div class="col">
            <input type="text" v-model="input"
              :class="'form-control ' + ($v.input.$model.length ? (!$v.input.required || !$v.input.validURL ? 'is-invalid' : 'is-valid') : '')"
              placeholder="Enter your url... and then press `Enter`"
              @keyup.enter="$v.input.required && $v.input.validURL && generateShortLink()"
            >
          </div>
        </div>
      </div>
    </div>

    <div class="recent" v-if="recentLinks.length">
      <div class="d-flex justify-content-between align-content-center mb-2">
        <h2>Recent shortened links</h2>
        <button class="btn" type="button" @click="clearRecent">Clear recent</button>
      </div>

      <div class="card mb-3" v-for="(recent, index) in recentLinks" :key="index">
        <div class="card-body">
          <div class="row align-items-center">
            <div class="col-auto">
              <button class="btn btn-icon btn-outline-primary" v-clipboard:copy="recent.short">
                <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="24" height="24"
                  viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                  stroke-linejoin="round">
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <rect x="8" y="8" width="12" height="12" rx="2"></rect>
                  <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
                </svg>
              </button>
            </div>
            <div class="col text-truncate">
              <p class="text-body d-block mb-0">{{ recent.short }}</p>
              <small class="d-block text-muted text-truncate mt-n1">{{ recent.origin }}</small>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { required } from 'vuelidate/lib/validators'

  const validURL = (str) => {
    let pattern = new RegExp('^(https?:\\/\\/)?' + // protocol
      '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
      '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
      '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
      '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
      '(\\#[-a-z\\d_]*)?$', 'i'); // fragment locator
    return !!pattern.test(str);
  }

  export default {
    name: 'Index',
    metaInfo: {
      title: 'Main page'
    },
    data() {
      return {
        input: '',
        recentLinks: []
      }
    },
    validations: {
      input: {
        required,
        validURL
      }
    },
    mounted() {
      this.recentLinks = JSON.parse(localStorage.getItem('recentLinks') ?? '[]')
    },
    methods: {
      clearRecent: function () {
        this.recentLinks = []
        localStorage.setItem('recentLinks', '[]')
      },
      generateShortLink: function () {
        // request to fastapi
        this.$axios.post('generate/', {
          origin: this.input
        }).then(response => {
          if (!response.data.success) return

          // save result for recentLinks
          this.recentLinks.unshift({
            origin: response.data.origin,
            short: `${ document.location.protocol }//${ document.location.hostname }/go/${ response.data.short }/`
          })

          this.input = ''

          localStorage.setItem('recentLinks', JSON.stringify(this.recentLinks))
        })
      }
    }
  }
</script>