import { readFiles } from 'h3'

export default defineEventHandler(async (event) => {
  try {
    const files = await readFiles(event, {
      includeFields: true,
    })

    if (!files || files.length === 0) {
      return {
        success: false,
        error: 'No file uploaded',
      }
    }

    const file = files[0]

    // Validate file type
    if (!file.name?.endsWith('.xml')) {
      return {
        success: false,
        error: 'Invalid file type. Please upload an XML file.',
      }
    }

    // Validate file size (max 10MB)
    const maxSize = 10 * 1024 * 1024
    if (file.data.length > maxSize) {
      return {
        success: false,
        error: 'File size exceeds 10MB limit',
      }
    }

    // Parse XML content
    const xmlContent = file.data.toString('utf-8')

    // Basic XML validation
    if (!xmlContent.trim().startsWith('<?xml') && !xmlContent.trim().startsWith('<')) {
      return {
        success: false,
        error: 'Invalid XML format',
      }
    }

    // Here you can add your XML processing logic
    // For now, we'll just return success with file info
    return {
      success: true,
      message: 'XML file uploaded successfully',
      data: {
        filename: file.name,
        size: file.data.length,
        preview: xmlContent.substring(0, 500), // First 500 characters
      },
    }
  }
  catch (error) {
    console.error('Upload error:', error)
    return {
      success: false,
      error: 'Failed to process file upload',
    }
  }
})
