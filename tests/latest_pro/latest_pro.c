/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * latest_pro.c
 * Copyright (C) 2023 Vladimir Roncevic <elektron.ronca@gmail.com>
 * 
 * latest_pro is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * latest_pro is distributed in the hope that it will be useful, but
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
#define    DEVICE_NAME      "latest_pro_cd"
#define    CLASS_NAME       "latest_pro"
#define    MSG_SIZE         256

static int major_number;
static char message[MSG_SIZE] = {0};
static short size_of_message;
static int number_opens = 0;
static struct class* latest_proCharClass = NULL;
static struct device* latest_proCharDevice = NULL;

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

static int __init latest_pro_init(void)
{
    printk(KERN_INFO "latest_pro_cd: Initializing the latest_pro_cd LKM\n");
    major_number = register_chrdev(0, DEVICE_NAME, &fops);

    if(major_number < 0)
    {
        printk(KERN_ALERT "latest_pro_cd failed to register a major number\n");
        return major_number;
    }

    printk(
        KERN_INFO "latest_pro_cd: registered correctly with major number %d\n",
        major_number
    );

    latest_proCharClass = class_create(THIS_MODULE, CLASS_NAME);

    if(IS_ERR(latest_proCharClass))
    {
        unregister_chrdev(major_number, DEVICE_NAME);
        printk(KERN_ALERT "Failed to register device class\n");
        return PTR_ERR(latest_proCharClass);
    }

    printk(KERN_INFO "latest_pro_cd: device class registered correctly\n");
    latest_proCharDevice = device_create(
        latest_proCharClass, NULL, MKDEV(major_number, 0), NULL, DEVICE_NAME
    );

    if(IS_ERR(latest_proCharDevice))
    {
        class_destroy(latest_proCharClass);
        unregister_chrdev(major_number, DEVICE_NAME);
        printk(KERN_ALERT "Failed to create the device\n");
        return PTR_ERR(latest_proCharDevice);
    }

    printk(KERN_INFO "latest_pro_cd: device class created correctly\n");

    return 0;
}

static void __exit latest_pro_exit(void)
{
    device_destroy(latest_proCharClass, MKDEV(major_number, 0));
    class_unregister(latest_proCharClass);
    class_destroy(latest_proCharClass);
    unregister_chrdev(major_number, DEVICE_NAME);
    printk(KERN_INFO "latest_pro_cd: goodbye from the LKM!\n");
}

static int dev_open(struct inode *inodep, struct file *filep)
{
    number_opens++;
    printk(
        KERN_INFO "latest_pro_cd: device has been opened %d time(s)\n",
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
            KERN_INFO "latest_pro_cd: sent %d characters to the user\n",
            size_of_message
        );

        return (size_of_message=0);
    }
    else
    {
        printk(
            KERN_INFO "latest_pro_cd: failed to send %d characters to the user\n",
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
        KERN_INFO "latest_pro_cd: received %zu characters from the user\n", len
    );

    return len;
}

static int dev_release(struct inode *inodep, struct file *filep)
{
    printk(KERN_INFO "latest_pro_cd: device successfully closed\n");
    return 0;
}

module_init(latest_pro_init);
module_exit(latest_pro_exit);

MODULE_AUTHOR(DRIVER_AUTHOR);
MODULE_DESCRIPTION(DRIVER_DESC);
MODULE_LICENSE(DRIVER_LICENSE);
MODULE_VERSION(DRIVER_VERSION);

