<script setup lang="ts">
const fileInput = ref<HTMLInputElement | null>(null)
const selectedFile = ref<File | null>(null)
const isUploading = ref(false)
const uploadResult = ref<any>(null)
const toast = useToast()

const handleFileSelect = (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]

  if (file) {
    if (!file.name.endsWith('.xml')) {
      toast.add({
        title: 'Invalid File Type',
        description: 'Please select an XML file',
        color: 'red',
      })
      return
    }

    selectedFile.value = file
    uploadResult.value = null
  }
}

const uploadFile = async () => {
  if (!selectedFile.value) {
    toast.add({
      title: 'No File Selected',
      description: 'Please select an XML file first',
      color: 'yellow',
    })
    return
  }

  isUploading.value = true
  uploadResult.value = null

  try {
    const formData = new FormData()
    formData.append('file', selectedFile.value)

    const response = await $fetch('/api/upload-xml', {
      method: 'POST',
      body: formData,
    })

    if (response.success) {
      toast.add({
        title: 'Upload Successful',
        description: response.message,
        color: 'green',
      })
      uploadResult.value = response.data
      selectedFile.value = null
      if (fileInput.value) {
        fileInput.value.value = ''
      }
    }
    else {
      toast.add({
        title: 'Upload Failed',
        description: response.error || 'An error occurred',
        color: 'red',
      })
    }
  }
  catch (error) {
    console.error('Upload error:', error)
    toast.add({
      title: 'Upload Error',
      description: 'Failed to upload file. Please try again.',
      color: 'red',
    })
  }
  finally {
    isUploading.value = false
  }
}

const clearFile = () => {
  selectedFile.value = null
  uploadResult.value = null
  if (fileInput.value) {
    fileInput.value.value = ''
  }
}
</script>

<template>
  <div class="w-full max-w-2xl mx-auto">
    <div class="border-2 border-dashed border-gray-300 dark:border-gray-700 rounded-lg p-8">
      <div class="text-center">
        <UIcon
          name="i-heroicons-document-arrow-up"
          class="mx-auto h-12 w-12 text-gray-400"
        />
        <div class="mt-4">
          <label
            for="file-upload"
            class="cursor-pointer"
          >
            <span class="mt-2 block text-sm font-semibold text-gray-900 dark:text-white">
              {{ selectedFile ? selectedFile.name : 'Select an XML file' }}
            </span>
            <input
              id="file-upload"
              ref="fileInput"
              type="file"
              accept=".xml"
              class="sr-only"
              @change="handleFileSelect"
            >
          </label>
          <p class="mt-1 text-xs text-gray-500 dark:text-gray-400">
            XML files up to 10MB
          </p>
        </div>

        <div class="mt-6 flex gap-3 justify-center">
          <UButton
            color="gray"
            variant="outline"
            @click="fileInput?.click()"
          >
            <UIcon name="i-heroicons-folder-open" />
            Browse Files
          </UButton>

          <UButton
            v-if="selectedFile"
            color="primary"
            :loading="isUploading"
            :disabled="!selectedFile || isUploading"
            @click="uploadFile"
          >
            <UIcon name="i-heroicons-arrow-up-tray" />
            Upload
          </UButton>

          <UButton
            v-if="selectedFile"
            color="red"
            variant="outline"
            :disabled="isUploading"
            @click="clearFile"
          >
            <UIcon name="i-heroicons-x-mark" />
            Clear
          </UButton>
        </div>
      </div>
    </div>

    <div
      v-if="uploadResult"
      class="mt-6 p-6 bg-green-50 dark:bg-green-950 rounded-lg border border-green-200 dark:border-green-800"
    >
      <h3 class="text-lg font-semibold text-green-900 dark:text-green-100 mb-4">
        <UIcon name="i-heroicons-check-circle" class="inline" />
        Upload Details
      </h3>
      <div class="space-y-2 text-sm">
        <p>
          <span class="font-medium text-green-900 dark:text-green-100">Filename:</span>
          <span class="text-green-700 dark:text-green-300 ml-2">{{ uploadResult.filename }}</span>
        </p>
        <p>
          <span class="font-medium text-green-900 dark:text-green-100">Size:</span>
          <span class="text-green-700 dark:text-green-300 ml-2">{{ (uploadResult.size / 1024).toFixed(2) }} KB</span>
        </p>
        <div v-if="uploadResult.preview">
          <p class="font-medium text-green-900 dark:text-green-100 mb-2">
            Preview:
          </p>
          <pre class="text-xs bg-white dark:bg-gray-900 p-3 rounded border border-green-200 dark:border-green-800 overflow-x-auto">{{ uploadResult.preview }}</pre>
        </div>
      </div>
    </div>
  </div>
</template>
