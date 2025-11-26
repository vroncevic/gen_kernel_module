/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * full_simple_new.c
 * Copyright (C) 2025 Vladimir Roncevic <elektron.ronca@gmail.com>
 * 
 * full_simple_new is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * full_simple_new is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#include <linux/init.h>
#include <linux/module.h>
#include <linux/device.h>
#include <linux/kernel.h>
#include <linux/uaccess.h>
#include <linux/fs.h>

#define    DRIVER_AUTHOR    "Vladimir Roncevic <elektron.ronca@gmail.com>"
#define    DRIVER_DESC      "LKM Character Driver"
#define    DRIVER_LICENSE   "GPL"
#define    DRIVER_VERSION   "1.0.0"
#define    DEVICE_NAME      "full_simple_new_cd"
#define    CLASS_NAME       "full_simple_new"
#define    MSG_SIZE         256

static int major_number;
static char message[MSG_SIZE] = {0};
static short size_of_message;
static int number_opens = 0;
static struct class* full_simple_newCharClass = NULL;
static struct device* full_simple_newCharDevice = NULL;

static int dev_open(struct inode*, struct file*);
static int dev_release(struct inode*, struct file*);
static ssize_t dev_read(struct file*, char*, size_t, loff_t*);
static ssize_t dev_write(struct file*, const char*, size_t, loff_t*);

static struct file_operations fops =
{
    .open = dev_open,
    .read = dev_read,
    .write = dev_write,
    .release = dev_release,
};

static int __init full_simple_new_init(void)
{
    printk(KERN_INFO "full_simple_new_cd: Initializing the full_simple_new_cd LKM\n");
    major_number = register_chrdev(0, DEVICE_NAME, &fops);

    if(major_number < 0)
    {
        printk(KERN_ALERT "full_simple_new_cd failed to register a major number\n");
        return major_number;
    }

    printk(
        KERN_INFO "full_simple_new_cd: registered correctly with major number %d\n",
        major_number
    );

    full_simple_newCharClass = class_create(THIS_MODULE, CLASS_NAME);

    if(IS_ERR(full_simple_newCharClass))
    {
        unregister_chrdev(major_number, DEVICE_NAME);
        printk(KERN_ALERT "Failed to register device class\n");
        return PTR_ERR(full_simple_newCharClass);
    }

    printk(KERN_INFO "full_simple_new_cd: device class registered correctly\n");
    full_simple_newCharDevice = device_create(
        full_simple_newCharClass, NULL, MKDEV(major_number, 0), NULL, DEVICE_NAME
    );

    if(IS_ERR(full_simple_newCharDevice))
    {
        class_destroy(full_simple_newCharClass);
        unregister_chrdev(major_number, DEVICE_NAME);
        printk(KERN_ALERT "Failed to create the device\n");
        return PTR_ERR(full_simple_newCharDevice);
    }

    printk(KERN_INFO "full_simple_new_cd: device class created correctly\n");

    return 0;
}

static void __exit full_simple_new_exit(void)
{
    device_destroy(full_simple_newCharClass, MKDEV(major_number, 0));
    class_unregister(full_simple_newCharClass);
    class_destroy(full_simple_newCharClass);
    unregister_chrdev(major_number, DEVICE_NAME);
    printk(KERN_INFO "full_simple_new_cd: goodbye from the LKM!\n");
}

static int dev_open(struct inode *inodep, struct file *filep)
{
    number_opens++;
    printk(
        KERN_INFO "full_simple_new_cd: device has been opened %d time(s)\n",
        number_opens
    );

    return 0;
}

static ssize_t dev_read(
    struct file *filep, char *buffer, size_t len, loff_t *offset
)
{
    int error_count = 0;
    error_count = copy_to_user(buffer, message, size_of_message);

    if(error_count==0)
    {
        printk(
            KERN_INFO "full_simple_new_cd: sent %d characters to the user\n",
            size_of_message
        );

        return (size_of_message=0);
    }
    else
    {
        printk(
            KERN_INFO "full_simple_new_cd: failed to send %d characters to the user\n",
            error_count
        );

        return -EFAULT;
    }
}

static ssize_t dev_write(
    struct file *filep, const char *buffer, size_t len, loff_t *offset
)
{
    sprintf(message, "%s(%zu letters)", buffer, len);
    size_of_message = strlen(message);

    printk(
        KERN_INFO "full_simple_new_cd: received %zu characters from the user\n", len
    );

    return len;
}

static int dev_release(struct inode *inodep, struct file *filep)
{
    printk(KERN_INFO "full_simple_new_cd: device successfully closed\n");
    return 0;
}

module_init(full_simple_new_init);
module_exit(full_simple_new_exit);

MODULE_AUTHOR(DRIVER_AUTHOR);
MODULE_DESCRIPTION(DRIVER_DESC);
MODULE_LICENSE(DRIVER_LICENSE);
MODULE_VERSION(DRIVER_VERSION);

