<template>
  <div id="app" class="page">
    <header class="navbar navbar-expand-md navbar-light d-print-none">
      <div class="container-xl">
        <h1 class="navbar-brand navbar-brand-autodark d-none-navbar-horizontal pe-0 pe-md-3 cursor-pointer">
          ShortLink
          <span class="badge bg-primary">beta</span>
        </h1>

        <div class="navbar-nav flex-row order-md-last">
          <div class="nav-item dropdown">
            <div class="nav-link d-flex lh-1 text-reset p-0 cursor-pointer">
              <div class="avatar bg-blue-lt">A</div>
              <div class="d-none d-xl-block ps-2">
                <div>Anonymous</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div class="content">
      <div class="container-xl">
        <router-view />
      </div>
    </div>
  </div>
</template>