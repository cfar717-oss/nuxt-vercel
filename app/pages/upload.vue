<script setup lang="ts">
definePageMeta({
  layout: false,
})

useSeoMeta({
  title: 'XML Upload',
  description: 'Upload and process XML files',
})
</script>

<template>
  <UApp>
    <NavbarTop />

    <div class="min-h-screen bg-gray-50 dark:bg-gray-900 py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto">
        <div class="text-center mb-12">
          <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-4">
            XML File Upload
          </h1>
          <p class="text-lg text-gray-600 dark:text-gray-400">
            Upload and process your XML files securely
          </p>
        </div>

        <div class="bg-white dark:bg-gray-800 shadow-lg rounded-lg p-8">
          <UploadXmlUploadForm />
        </div>

        <div class="mt-8 bg-blue-50 dark:bg-blue-950 rounded-lg p-6 border border-blue-200 dark:border-blue-800">
          <h2 class="text-lg font-semibold text-blue-900 dark:text-blue-100 mb-3">
            <UIcon name="i-heroicons-information-circle" class="inline" />
            Upload Guidelines
          </h2>
          <ul class="space-y-2 text-sm text-blue-800 dark:text-blue-200">
            <li class="flex items-start">
              <UIcon name="i-heroicons-check-circle" class="mr-2 mt-0.5 flex-shrink-0" />
              <span>Only XML files (.xml extension) are accepted</span>
            </li>
            <li class="flex items-start">
              <UIcon name="i-heroicons-check-circle" class="mr-2 mt-0.5 flex-shrink-0" />
              <span>Maximum file size is 10MB</span>
            </li>
            <li class="flex items-start">
              <UIcon name="i-heroicons-check-circle" class="mr-2 mt-0.5 flex-shrink-0" />
              <span>Files must be valid XML format</span>
            </li>
            <li class="flex items-start">
              <UIcon name="i-heroicons-check-circle" class="mr-2 mt-0.5 flex-shrink-0" />
              <span>You'll see a preview of your uploaded content</span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <TheFooter />
  </UApp>
</template>
